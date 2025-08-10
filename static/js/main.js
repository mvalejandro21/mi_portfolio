document.addEventListener('DOMContentLoaded', function() {
    // Tema claro/oscuro
    const themeToggle = document.querySelector('.theme-toggle');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // Comprobar preferencias del sistema
    if (prefersDarkScheme.matches) {
        document.body.classList.add('dark-mode');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }
    
    // Alternar tema
    themeToggle.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
        
        if (document.body.classList.contains('dark-mode')) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        } else {
            themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        }
    });
    
    // Menú móvil
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    const blurOverlay = document.querySelector('.blur-overlay');
    
    mobileMenuToggle.addEventListener('click', function() {
        this.classList.toggle('active');
        navLinks.classList.toggle('show');
        blurOverlay.classList.toggle('active');
        document.body.classList.toggle('no-scroll');
    });
    
    blurOverlay.addEventListener('click', function() {
        mobileMenuToggle.classList.remove('active');
        navLinks.classList.remove('show');
        this.classList.remove('active');
        document.body.classList.remove('no-scroll');
    });
    
    // Efecto de scroll en navbar
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.glass-navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Animaciones al hacer scroll
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });
    
    animateElements.forEach(el => observer.observe(el));
    
    // Año actual en footer
    document.getElementById('current-year').textContent = new Date().getFullYear();
    
    // Efecto hover en tarjetas de habilidades
    const skillCards = document.querySelectorAll('.skill-card');
    
    skillCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            const icon = this.querySelector('i');
            icon.classList.add('animate__animated', 'animate__pulse');
            
            icon.addEventListener('animationend', function() {
                icon.classList.remove('animate__animated', 'animate__pulse');
            }, { once: true });
        });
    });
    
    // Smooth scroll para enlaces internos
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
                
                // Cerrar menú móvil si está abierto
                if (navLinks.classList.contains('show')) {
                    mobileMenuToggle.classList.remove('active');
                    navLinks.classList.remove('show');
                    blurOverlay.classList.remove('active');
                    document.body.classList.remove('no-scroll');
                }
            }
        });
    });
});