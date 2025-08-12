// ==========================
// UTILITY FUNCTIONS
// ==========================
const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

const throttle = (func, limit) => {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
};

// ==========================
// DOM CONTENT LOADED
// ==========================
document.addEventListener('DOMContentLoaded', function() {
  initializePortfolio();
});

// ==========================
// MAIN INITIALIZATION
// ==========================
function initializePortfolio() {
  try {
    initializeNavigation();
    initializeAnimations();
    initializeSkills();
    initializeContactForm();
    initializeScrollEffects();
    initializeAccessibility();
  } catch (error) {
    console.error('Portfolio initialization error:', error);
  }
}

// ==========================
// MOBILE NAVIGATION
// ==========================
function initializeNavigation() {
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  
  if (!navToggle || !navLinks) return;
  
  navToggle.addEventListener('click', () => {
    const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', !isExpanded);
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
  });
  
  // Close mobile menu when clicking on a link
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('active');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
  
  // Close mobile menu when clicking outside
  document.addEventListener('click', (e) => {
    if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
      navToggle.classList.remove('active');
      navLinks.classList.remove('active');
      navToggle.setAttribute('aria-expanded', 'false');
    }
  });
}

// ==========================
// SMOOTH SCROLLING
// ==========================
function initializeSmoothScrolling() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const target = document.querySelector(targetId);
      
      if (target) {
        const headerHeight = document.querySelector('.header').offsetHeight;
        const targetPosition = target.offsetTop - headerHeight - 20;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// ==========================
// ANIMATIONS INITIALIZATION
// ==========================
function initializeAnimations() {
  // Initialize AOS
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 1000,
      once: true,
      easing: 'ease-in-out',
      offset: 100,
      delay: 0
    });
  }
  
  // Initialize GSAP animations
  if (typeof gsap !== 'undefined') {
    initializeGSAPAnimations();
  }
  
  // Initialize typing animation
  initializeTypingAnimation();
}

// ==========================
// GSAP ANIMATIONS
// ==========================
function initializeGSAPAnimations() {
  // Hero animations
  const heroTimeline = gsap.timeline();
  
  heroTimeline
    .from(".hero-title", {
      y: 50,
      opacity: 0,
      duration: 1,
      ease: "power3.out"
    })
    .from(".hero-subtitle", {
      y: 30,
      opacity: 0,
      duration: 1,
      ease: "power3.out"
    }, "-=0.5")
    .from(".hero-buttons", {
      y: 30,
      opacity: 0,
      duration: 0.8,
      ease: "power3.out"
    }, "-=0.3");
  
  // Floating animations for skill cards
  initializeFloatingAnimations();
  
  // Project card hover effects
  initializeProjectHoverEffects();
  
  // Timeline animations
  initializeTimelineAnimations();
}

// ==========================
// FLOATING ANIMATIONS
// ==========================
function initializeFloatingAnimations() {
  const skillCards = document.querySelectorAll('.skill-card');
  
  skillCards.forEach((card, index) => {
    gsap.to(card, {
      y: -10,
      duration: 2,
      repeat: -1,
      yoyo: true,
      ease: "easeInOut",
      delay: index * 0.2
    });
  });
}

// ==========================
// PROJECT HOVER EFFECTS
// ==========================
function initializeProjectHoverEffects() {
  document.querySelectorAll(".project-card").forEach(card => {
    card.addEventListener("mouseenter", () => {
      gsap.to(card, { 
        boxShadow: "0 0 25px rgba(0, 247, 255, 0.4)", 
        duration: 0.4 
      });
    });
    
    card.addEventListener("mouseleave", () => {
      gsap.to(card, { 
        boxShadow: "0 0 0px transparent", 
        duration: 0.4 
      });
    });
  });
}

// ==========================
// TIMELINE ANIMATIONS
// ==========================
function initializeTimelineAnimations() {
  if (typeof ScrollTrigger !== 'undefined') {
    gsap.utils.toArray(".timeline-item").forEach(item => {
      gsap.from(item, {
        scrollTrigger: {
          trigger: item,
          start: "top 85%",
          toggleActions: "play none none reset"
        },
        opacity: 0,
        y: 30,
        duration: 0.8
      });
    });
  }
}

// ==========================
// SKILLS ANIMATIONS
// ==========================
function initializeSkills() {
  const skillBars = document.querySelectorAll('.skill-bar');
  
  const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const skillBar = entry.target;
        const width = skillBar.getAttribute('data-width');
        
        gsap.to(skillBar, {
          width: `${width}%`,
          duration: 1.5,
          ease: "power2.out"
        });
        
        skillObserver.unobserve(skillBar);
      }
    });
  }, observerOptions);
  
  skillBars.forEach(bar => {
    skillObserver.observe(bar);
  });
}

// ==========================
// TYPING ANIMATION
// ==========================
function initializeTypingAnimation() {
  const heroTitle = document.querySelector('.hero-title');
  if (!heroTitle) return;
  
  const originalText = heroTitle.textContent;
  const typingSpeed = 80;
  let i = 0;
  
  function typeWriter() {
    if (i < originalText.length) {
      heroTitle.textContent = originalText.substring(0, i + 1);
      i++;
      setTimeout(typeWriter, typingSpeed);
    }
  }
  
  // Start typing animation after a delay
  setTimeout(typeWriter, 1000);
}

// ==========================
// SCROLL EFFECTS
// ==========================
function initializeScrollEffects() {
  // Navigation highlighting
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');
  
  const updateActiveNav = throttle(() => {
    let current = '';
    const scrollPosition = window.scrollY + 200;
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });
    
    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }, 100);
  
  window.addEventListener('scroll', updateActiveNav);
  
  // Parallax effect for hero background
  const heroBackground = document.querySelector('.hero-background');
  if (heroBackground) {
    window.addEventListener('scroll', throttle(() => {
      const scrolled = window.pageYOffset;
      const rate = scrolled * -0.5;
      heroBackground.style.transform = `translateY(${rate}px)`;
    }, 16));
  }
}

// ==========================
// CONTACT FORM
// ==========================
function initializeContactForm() {
  const contactForm = document.getElementById('contactForm');
  if (!contactForm) return;
  
  contactForm.addEventListener('submit', handleFormSubmission);
  
  // Real-time validation
  const inputs = contactForm.querySelectorAll('input, textarea');
  inputs.forEach(input => {
    input.addEventListener('blur', validateField);
    input.addEventListener('input', clearFieldError);
  });
}

async function handleFormSubmission(e) {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const formObject = Object.fromEntries(formData);
  
  // Validate all fields
  const isValid = validateForm(formObject);
  if (!isValid) return;
  
  // Show loading state
  const submitBtn = e.target.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  submitBtn.textContent = 'Sending...';
  submitBtn.disabled = true;
  
  try {
    // Send to backend API
    const response = await fetch('/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formObject)
    });
    
    const result = await response.json();
    
    if (result.success) {
      showNotification(result.message, 'success');
      e.target.reset();
    } else {
      showNotification(result.message, 'error');
    }
  } catch (error) {
    console.error('Form submission error:', error);
    showNotification('Network error. Please try again later.', 'error');
  } finally {
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
  }
}

function validateForm(data) {
  const required = ['name', 'email', 'subject', 'message'];
  let isValid = true;
  
  required.forEach(field => {
    if (!data[field] || data[field].trim() === '') {
      showFieldError(field, 'This field is required');
      isValid = false;
    }
  });
  
  if (data.email && !isValidEmail(data.email)) {
    showFieldError('email', 'Please enter a valid email address');
    isValid = false;
  }
  
  return isValid;
}

function validateField(e) {
  const field = e.target;
  const value = field.value.trim();
  const fieldName = field.name;
  
  if (!value) {
    showFieldError(fieldName, 'This field is required');
  } else if (fieldName === 'email' && !isValidEmail(value)) {
    showFieldError(fieldName, 'Please enter a valid email address');
  } else {
    clearFieldError(e);
  }
}

function showFieldError(fieldName, message) {
  const field = document.querySelector(`[name="${fieldName}"]`);
  if (!field) return;
  
  field.classList.add('error');
  
  let errorElement = field.parentNode.querySelector('.field-error');
  if (!errorElement) {
    errorElement = document.createElement('div');
    errorElement.className = 'field-error';
    field.parentNode.appendChild(errorElement);
  }
  errorElement.textContent = message;
}

function clearFieldError(e) {
  const field = e.target;
  field.classList.remove('error');
  
  const errorElement = field.parentNode.querySelector('.field-error');
  if (errorElement) {
    errorElement.remove();
  }
}

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// ==========================
// NOTIFICATION SYSTEM
// ==========================
function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotification = document.querySelector('.notification');
  if (existingNotification) {
    existingNotification.remove();
  }
  
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification notification-${type}`;
  notification.setAttribute('role', 'alert');
  notification.setAttribute('aria-live', 'polite');
  
  const colors = {
    success: '#00f7ff',
    error: '#ff4757',
    info: '#3742fa'
  };
  
  notification.innerHTML = `
    <span>${message}</span>
    <button class="notification-close" aria-label="Close notification">&times;</button>
  `;
  
  // Add styles
  Object.assign(notification.style, {
    position: 'fixed',
    top: '20px',
    right: '20px',
    padding: '15px 20px',
    borderRadius: '8px',
    color: 'white',
    fontWeight: '600',
    zIndex: '10000',
    display: 'flex',
    alignItems: 'center',
    gap: '10px',
    animation: 'slideInRight 0.3s ease',
    maxWidth: '400px',
    background: colors[type] || colors.info,
    boxShadow: '0 4px 12px rgba(0,0,0,0.3)'
  });
  
  // Add close button functionality
  const closeBtn = notification.querySelector('.notification-close');
  closeBtn.addEventListener('click', () => {
    notification.remove();
  });
  
  // Add to page
  document.body.appendChild(notification);
  
  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.style.animation = 'slideOutRight 0.3s ease';
      setTimeout(() => notification.remove(), 300);
    }
  }, 5000);
}

// ==========================
// ACCESSIBILITY
// ==========================
function initializeAccessibility() {
  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const navToggle = document.getElementById('navToggle');
      if (navToggle && navToggle.classList.contains('active')) {
        navToggle.click();
      }
    }
  });
  
  // Focus management
  const focusableElements = document.querySelectorAll(
    'a, button, input, textarea, select, [tabindex]:not([tabindex="-1"])'
  );
  
  focusableElements.forEach(element => {
    element.addEventListener('focus', () => {
      element.style.outline = '2px solid var(--primary-color)';
    });
    
    element.addEventListener('blur', () => {
      element.style.outline = 'none';
    });
  });
  
  // Smooth scrolling for keyboard navigation
  initializeSmoothScrolling();
}

// ==========================
// PERFORMANCE OPTIMIZATIONS
// ==========================
// Lazy load images
function initializeLazyLoading() {
  const images = document.querySelectorAll('img[data-src]');
  
  const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        imageObserver.unobserve(img);
      }
    });
  });
  
  images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeLazyLoading);
} else {
  initializeLazyLoading();
}
  