"""Main application routes."""

from datetime import datetime
import json
import logging
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_validator import validate_email, EmailNotValidError

from flask import Blueprint, current_app, jsonify, render_template, request, send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

bp = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

# Rate limiting for contact form
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["5 per hour"],
    storage_uri="memory://",
)


@bp.route('/')
def index():
    """Render the portfolio landing page."""
    return render_template('index.html')


@bp.route('/api/contact', methods=['POST'])
@limiter.limit("5 per hour")
def contact():
    """Handle contact form submissions with rate limiting and validation."""
    try:
        data = request.get_json(silent=True) or {}

        # Validate required fields
        required_fields = {
            'name': 'Name is required',
            'email': 'Email is required',
            'subject': 'Subject is required',
            'message': 'Message is required'
        }

        for field, error_msg in required_fields.items():
            value = (data.get(field) or '').strip()
            if not value:
                return jsonify({'success': False, 'message': error_msg}), 400

        # Validate email format
        try:
            email = validate_email(data['email'].strip()).email
        except EmailNotValidError as e:
            return jsonify({'success': False, 'message': str(e)}), 400

        # Save contact submission (optional persistence)
        submission_id = _save_contact_submission(data)

        # Prepare and send email
        subject = f"Portfolio Contact: {data['subject']}"
        body = f"""
        New contact form submission from your portfolio website:

        Name: {data['name']}
        Email: {email}
        Subject: {data['subject']}
        Message: {data['message']}

        Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Submission ID: {submission_id}
        """

        if _send_email(subject, body):
            logger.info("Contact form submitted successfully by %s (%s)", data['name'], email)
            return jsonify({
                'success': True,
                'message': "Message sent successfully! I'll get back to you soon.",
                'submission_id': submission_id
            })

        logger.error("Failed to send contact form email from %s", email)
        return jsonify({
            'success': False,
            'message': 'Failed to send message. Please try again later.'
        }), 500

    except Exception as e:
        logger.exception('Error processing contact form: %s', str(e))
        return jsonify({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }), 500


@bp.route('/api/health')
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })


@bp.route('/api/config')
def get_config():
    """Get public configuration (non-sensitive)."""
    return jsonify({
        'contact_enabled': bool(current_app.config.get('MAIL_USERNAME')),
        'rate_limit_contact': current_app.config.get('RATELIMIT_CONTACT', '5 per hour'),
        'debug': current_app.debug
    })


@bp.route('/api/stats')
def get_stats():
    """Get application statistics."""
    # In a real app, this would come from a database
    return jsonify({
        'total_visits': 0,  # Would be tracked in a real app
        'contact_submissions': 0,  # Would be counted from database
        'uptime': '0 days',  # Would calculate actual uptime
        'last_updated': datetime.now().isoformat()
    })


# Static file routes for backward compatibility
@bp.route('/styles.css')
def styles_css():
    """Serve styles.css for backward compatibility."""
    return send_from_directory('static/css', 'styles.css')


@bp.route('/script.js')
def script_js():
    """Serve script.js for backward compatibility."""
    return send_from_directory('static/js', 'script.js')


@bp.route('/<path:filename>')
def static_files(filename):
    """Serve static files (CSS, JS, images)."""
    if filename.endswith('.css'):
        return send_from_directory('static/css', filename)
    elif filename.endswith('.js'):
        return send_from_directory('static/js', filename)
    elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg')):
        return send_from_directory('static/img', filename)
    else:
        return send_from_directory('static', filename)


def _save_contact_submission(data: dict) -> str:
    """Save contact submission to file (optional persistence)."""
    try:
        # Create submissions directory
        submissions_dir = os.path.join(current_app.root_path, '..', 'submissions')
        os.makedirs(submissions_dir, exist_ok=True)

        # Generate unique ID
        submission_id = f"contact_{int(datetime.now().timestamp())}_{hash(data['email']) % 1000}"

        # Save submission
        submission_file = os.path.join(submissions_dir, f'{submission_id}.json')
        with open(submission_file, 'w') as f:
            json.dump({
                'id': submission_id,
                'timestamp': datetime.now().isoformat(),
                'name': data['name'],
                'email': data['email'],
                'subject': data['subject'],
                'message': data['message'],
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent', '')
            }, f, indent=2)

        logger.info("Contact submission saved: %s", submission_id)
        return submission_id

    except Exception as e:
        logger.error("Failed to save contact submission: %s", str(e))
        # Generate a fallback ID even if saving fails
        return f"contact_{int(datetime.now().timestamp())}"


def _send_email(subject: str, body: str) -> bool:
    """Send email using SMTP settings from app configuration."""
    cfg = current_app.config

    mail_username = cfg.get('MAIL_USERNAME')
    mail_password = cfg.get('MAIL_PASSWORD')
    mail_server = cfg.get('MAIL_SERVER')
    mail_port = cfg.get('MAIL_PORT')
    recipient = cfg.get('MAIL_DEFAULT_RECIPIENT') or mail_username

    if not all([mail_username, mail_password, mail_server, recipient]):
        logger.error('Email configuration is incomplete. Check environment variables.')
        return False

    try:
        msg = MIMEMultipart()
        msg['From'] = mail_username
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(mail_server, mail_port) as server:
            if cfg.get('MAIL_USE_TLS', True):
                server.starttls()
            server.login(mail_username, mail_password)
            server.send_message(msg)

        return True
    except Exception as e:
        logger.exception('Email sending failed: %s', str(e))
        return False
