document.addEventListener('DOMContentLoaded', () => {
    const fadeElements = document.querySelectorAll('.fade-in-left, .fade-in-right, .fade-in-card');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                const el = entry.target;

                // Optional: stagger the delay on cards
                if (el.classList.contains('fade-in-card')) {
                    el.style.transitionDelay = `${index * 0.1}s`;
                }

                el.classList.add('in-view');
                observer.unobserve(el); // Remove if you want to re-trigger
            }
        });
    }, {
        threshold: 0.2,
        rootMargin: '-100px 0px',
    });

    fadeElements.forEach(el => observer.observe(el));
});
