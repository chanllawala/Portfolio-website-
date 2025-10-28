"""Application factory for the portfolio project."""

import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import get_config


def create_app(config_class=None) -> Flask:
    """Create and configure a Flask application instance."""
    if config_class is None:
        config_class = get_config()

    app = Flask(
        __name__,
        static_folder='static',
        template_folder='templates'
    )

    app.config.from_object(config_class)

    # Validate configuration
    config_errors = config_class.validate()
    if config_errors:
        app.logger.error("Configuration errors: %s", config_errors)
        if not app.debug:
            raise RuntimeError(f"Configuration errors: {config_errors}")
        else:
            # In debug mode, warn but don't fail
            app.logger.warning("Configuration errors (continuing in debug mode): %s", config_errors)

    # Configure logging
    _configure_logging(app)

    # Configure rate limiting
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=[app.config.get('RATELIMIT_DEFAULT', '200 per day, 50 per hour')],
        storage_uri="memory://",
    )

    # Register error handlers
    _register_error_handlers(app)

    # Register blueprints
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    app.logger.info("Portfolio application created successfully")
    return app


def _configure_logging(app: Flask) -> None:
    """Configure logging for the application."""
    if not app.debug:
        # Production logging
        if not app.logger.handlers:
            # Create logs directory
            logs_dir = os.path.join(app.root_path, '..', 'logs')
            os.makedirs(logs_dir, exist_ok=True)

            # File handler
            file_handler = RotatingFileHandler(
                os.path.join(logs_dir, 'portfolio.log'),
                maxBytes=10240000,  # 10MB
                backupCount=10
            )
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            ))
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)

            # Also log to console
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            app.logger.addHandler(console_handler)
    else:
        # Development logging - use Flask's default development logging
        logging.basicConfig(level=logging.DEBUG)


def _register_error_handlers(app: Flask) -> None:
    """Register error handlers for the application."""

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        app.logger.warning(f"404 error: {error}")
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        app.logger.error(f"500 error: {error}")
        return render_template('errors/500.html'), 500

    @app.errorhandler(429)
    def rate_limit_error(error):
        """Handle rate limit errors."""
        app.logger.warning(f"Rate limit exceeded: {error}")
        return {
            'success': False,
            'message': 'Too many requests. Please try again later.'
        }, 429
