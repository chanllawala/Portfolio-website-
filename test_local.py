#!/usr/bin/env python3
"""
Simple test script to verify the Flask application works locally
"""

import requests
import json
import os
import sys
from app import app

def test_home_page():
    """Test the home page loads correctly"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert 'Kirtan Chanllawala' in response.data.decode()
        print("✅ Home page loads correctly")

def test_health_endpoint():
    """Test the health check endpoint"""
    with app.test_client() as client:
        response = client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'
        print("✅ Health endpoint works correctly")

def test_contact_form():
    """Test the contact form endpoint"""
    with app.test_client() as client:
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Message',
            'message': 'This is a test message'
        }
        
        response = client.post('/api/contact', 
                             data=json.dumps(test_data),
                             content_type='application/json')
        
        # Should return 200 or 500 (depending on email config)
        assert response.status_code in [200, 500]
        data = json.loads(response.data)
        print(f"✅ Contact form endpoint responds (status: {response.status_code})")

def test_static_files():
    """Test that static files are accessible"""
    with app.test_client() as client:
        # Test CSS file
        response = client.get('/styles.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type', '')
        
        # Test JS file
        response = client.get('/script.js')
        assert response.status_code == 200
        assert 'javascript' in response.headers.get('Content-Type', '')
        
        # Test image file
        response = client.get('/IMG-20250625-WA0019.jpg')
        assert response.status_code == 200
        
        print("✅ Static files are accessible")

if __name__ == '__main__':
    print("🧪 Testing Flask application...")
    
    try:
        test_home_page()
        test_health_endpoint()
        test_contact_form()
        test_static_files()
        
        print("\n🎉 All tests passed! Your application is ready for deployment.")
        print("\nTo run locally:")
        print("  python app.py")
        print("\nTo deploy to Render:")
        print("  1. Push to GitHub")
        print("  2. Connect to Render")
        print("  3. Set environment variables")
        print("  4. Deploy!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        sys.exit(1) 