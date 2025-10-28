# Kirtan Chanllawala - Portfolio Website

A modern, responsive portfolio website with a Flask backend, showcasing my skills, experience, and projects. Built with performance, accessibility, and SEO in mind.

## ✨ Features

- **🚀 Performance Optimized** - Fast loading with lazy loading and optimized animations
- **📱 Fully Responsive** - Perfect on all devices and screen sizes
- **♿ Accessibility Compliant** - WCAG guidelines with keyboard navigation and screen reader support
- **🔍 SEO Optimized** - Structured data, meta tags, and semantic HTML
- **🎨 Modern Animations** - GSAP-powered smooth animations and transitions
- **📊 Interactive Skills** - Animated progress bars and skill categories
- **📝 Working Contact Form** - Real backend integration with email notifications
- **🔒 Security Enhanced** - Rate limiting, input validation, and secure configuration
- **📧 Email Functionality** - Contact form sends emails to your inbox
- **🌐 Social Integration** - Prominent LinkedIn integration
- **🎓 Education Showcase** - University of Stirling graduation highlights
- **📈 Application Monitoring** - Health checks and logging
- **🔧 Development Tools** - Testing suite and development configuration

## 🚀 Recent Improvements

- **Enhanced Backend Architecture** - Modular Flask application with blueprints
- **Rate Limiting** - Protection against spam and abuse (5 requests/hour for contact form)
- **Email Validation** - Professional email validation with error handling
- **Configuration Management** - Environment-based configuration with validation
- **Error Handling** - Custom 404/500 error pages with proper logging
- **Contact Persistence** - Optional saving of contact submissions to JSON files
- **API Endpoints** - Additional endpoints for configuration and statistics
- **Logging System** - Comprehensive logging with file rotation and different levels
- **Development/Production Modes** - Different configurations for different environments

## 🛠️ Technical Stack

### Frontend
- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Modern styling with CSS Grid, Flexbox, and CSS Variables
- **JavaScript (ES6+)** - Modular code with performance optimizations
- **GSAP** - Professional animations and transitions
- **AOS** - Scroll-triggered animations
- **Intersection Observer** - Performance-optimized scroll effects

### Backend
- **Python Flask** - Lightweight web framework with modular architecture
- **Flask-Limiter** - Rate limiting for API protection
- **Email-Validator** - Professional email validation
- **Gunicorn** - Production WSGI server
- **SMTP** - Email functionality for contact form
- **Render** - Free hosting platform

## 📁 File Structure

```
Portfolio website/
├── app.py                    # Main Flask application entry point
├── portfolio/                # Main application package
│   ├── __init__.py          # Application factory and configuration
│   ├── routes.py            # Route definitions and API endpoints
│   ├── static/              # Static assets (CSS, JS, images)
│   │   ├── css/
│   │   │   └── styles.css   # Main stylesheet
│   │   ├── js/
│   │   │   └── script.js    # Frontend JavaScript
│   │   └── img/             # Images and media files
│   └── templates/           # Jinja2 templates
│       ├── index.html       # Main portfolio page
│       └── errors/          # Error page templates
│           ├── 404.html     # Not found page
│           └── 500.html     # Server error page
├── config.py                # Configuration management
├── requirements.txt         # Python dependencies
├── render.yaml              # Render deployment configuration
├── .env                     # Environment variables (not in git)
├── logs/                    # Application logs (created at runtime)
├── submissions/             # Contact form submissions (created at runtime)
├── test_local.py            # Local testing suite
├── .gitignore               # Git ignore file
└── README.md                # Project documentation
```

## 🚀 Quick Deployment

### Option 1: Deploy to Render (Recommended)
{{ ... }}
1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/portfolio.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [Render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
   - Set environment variables for email
   - Deploy!

### Option 2: Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export MAIL_USERNAME=your-email@gmail.com
   export MAIL_PASSWORD=your-app-password
   export SECRET_KEY=your-secret-key
   ```

3. **Run locally:**
   ```bash
   python app.py
   ```

## 📧 Email Setup

The contact form sends emails to your inbox. To set up:

1. **Enable 2FA on Gmail**
2. **Generate App Password**
3. **Set environment variables in Render:**
   ```
   MAIL_USERNAME = your-email@gmail.com
   MAIL_PASSWORD = your-app-password
   MAIL_SERVER = smtp.gmail.com
   MAIL_PORT = 587
   SECRET_KEY = your-secret-key
   ```

## 🚀 Performance Features

- **Resource Preloading** - Critical CSS and fonts preloaded
- **Lazy Loading** - Images load only when needed
- **Debounced Events** - Optimized scroll and resize handlers
- **Throttled Animations** - Smooth performance on all devices
- **Minified Dependencies** - CDN-hosted libraries for speed
- **Backend Caching** - Efficient static file serving

## ♿ Accessibility Features

- **Keyboard Navigation** - Full keyboard support
- **Screen Reader Support** - ARIA labels and semantic HTML
- **Focus Management** - Clear focus indicators
- **Skip Links** - Quick navigation for assistive technology
- **Color Contrast** - WCAG AA compliant color scheme

## 📊 Skills Section

The skills section now features:
- **Categorized Skills** - Programming Languages, Web Development, and Specialized Technologies
- **Progress Bars** - Animated skill level indicators
- **Hover Effects** - Interactive skill cards
- **Responsive Grid** - Adapts to different screen sizes

## 📝 Contact Form

Enhanced contact form with:
- **Real Backend Integration** - Sends actual emails
- **Real-time Validation** - Instant feedback on form errors
- **Accessibility** - Proper labels and error messages
- **Loading States** - Visual feedback during submission
- **Success Notifications** - User-friendly confirmation messages

## 🎓 Education Section

Showcases your academic achievements:
- **University of Stirling** - Computer Science degree
- **Graduation Photo** - Professional presentation
- **Structured Data** - SEO-optimized education information

## 🔧 Customization

### Update Project Links
In the Projects section, update the demo and source code links:
- Replace `#` with actual URLs for your project demos
- Replace `#` with actual URLs for your project source code

### Modify Skills
Update skill percentages in `templates/index.html`:
```html
<span class="skill-level">90%</span>
```

### Change Colors
Update CSS variables in `styles.css`:
```css
:root {
  --primary-color: #00f7ff;
  --secondary-color: #ff00f7;
}
```

## 📈 SEO Features

- **Structured Data** - Schema.org markup for better search results
- **Meta Tags** - Comprehensive Open Graph and Twitter cards
- **Semantic HTML** - Proper heading hierarchy and landmarks
- **Performance** - Fast loading times for better rankings

## 🎨 Design Features

- **Modern Dark Theme** - Professional appearance
- **Cyan Accent Color** - Consistent brand identity
- **Smooth Animations** - Engaging user experience
- **Responsive Typography** - Scales perfectly on all devices

## 📱 Mobile Features

- **Hamburger Menu** - Touch-friendly navigation
- **Touch Gestures** - Smooth scrolling and interactions
- **Optimized Images** - Fast loading on mobile networks
- **Responsive Layout** - Perfect on all screen sizes

## 🔗 Social Integration

- **LinkedIn Profile** - Prominently featured with custom styling
- **Professional Branding** - Consistent across all platforms
- **Easy Sharing** - Optimized for social media platforms

## 📞 Contact

- **LinkedIn**: [Kirtan Chanllawala](https://www.linkedin.com/in/kirtan-chanllawala-18b755230/)
- **Email**: kchanllawala@gmail.com
- **Location**: Available for remote work worldwide

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For deployment help, see [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

**Built with ❤️ and modern web technologies**

**Live Demo**: [Your Render URL here] 🚀 