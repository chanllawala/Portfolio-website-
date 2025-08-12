# Portfolio Deployment Guide - Render

This guide will help you deploy your portfolio website to Render with a working contact form.

## 🚀 Quick Deploy to Render

### Step 1: Prepare Your Repository

1. **Create a GitHub repository** and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/portfolio.git
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +"** and select **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service:**
   - **Name**: `kirtan-portfolio` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

### Step 3: Set Up Email Configuration

#### Option A: Gmail (Recommended)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password:**
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a new app password for "Mail"
3. **Set Environment Variables in Render:**
   - Go to your service dashboard
   - Click "Environment" tab
   - Add these variables:
     ```
     MAIL_USERNAME = your-email@gmail.com
     MAIL_PASSWORD = your-app-password
     MAIL_SERVER = smtp.gmail.com
     MAIL_PORT = 587
     SECRET_KEY = your-secret-key-here
     ```

#### Option B: Other Email Providers

For other providers, update the environment variables accordingly:
- **Outlook**: `smtp-mail.outlook.com:587`
- **Yahoo**: `smtp.mail.yahoo.com:587`

### Step 4: Deploy

1. **Click "Create Web Service"**
2. **Wait for deployment** (usually 2-3 minutes)
3. **Your site will be live** at: `https://your-app-name.onrender.com`

## 📧 Email Setup Details

### Gmail App Password Setup

1. **Sign in to your Google Account**
2. **Go to Security settings**
3. **Enable 2-Step Verification** if not already enabled
4. **Generate App Password:**
   - Select "Mail" as the app
   - Copy the 16-character password
5. **Use this password** in the `MAIL_PASSWORD` environment variable

### Testing Email Functionality

1. **Deploy your site**
2. **Go to the contact form**
3. **Fill out and submit** a test message
4. **Check your email** for the received message

## 🔧 Custom Domain (Optional)

### Step 1: Buy a Domain
- Purchase from providers like Namecheap, GoDaddy, or Google Domains

### Step 2: Configure DNS
1. **In your domain provider's DNS settings:**
   - Add a CNAME record:
     - **Name**: `@` or `www`
     - **Value**: `your-app-name.onrender.com`

### Step 3: Add to Render
1. **In your Render service dashboard:**
   - Go to "Settings" → "Custom Domains"
   - Add your domain
   - Follow the verification steps

## 🛠️ Troubleshooting

### Common Issues

1. **Build Fails:**
   - Check that `requirements.txt` is in the root directory
   - Ensure all dependencies are listed

2. **Email Not Working:**
   - Verify Gmail app password is correct
   - Check environment variables are set
   - Ensure 2FA is enabled on Gmail

3. **Static Files Not Loading:**
   - Ensure all files are in the correct directories
   - Check file permissions

### Debug Mode

To debug locally:
```bash
python app.py
```

## 📁 File Structure

```
portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── render.yaml           # Render configuration
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── styles.css        # CSS styles
│   ├── script.js         # JavaScript
│   ├── favicon.svg       # Favicon
│   └── IMG-20250625-WA0019.jpg  # Graduation photo
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

## 🔒 Security Notes

- **Never commit** your email password to Git
- **Use environment variables** for sensitive data
- **Keep your SECRET_KEY** secure and unique
- **Regularly update** dependencies

## 📈 Performance Tips

- **Enable caching** for static files
- **Optimize images** before uploading
- **Use CDN** for external libraries
- **Monitor** your Render usage

## 🆘 Support

If you encounter issues:
1. **Check Render logs** in your service dashboard
2. **Verify environment variables** are set correctly
3. **Test locally** first
4. **Check Render documentation** for platform-specific issues

---

**Your portfolio will be live at: `https://your-app-name.onrender.com`** 🎉 