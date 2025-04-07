// document.addEventListener('DOMContentLoaded', () => {
//     const elements = document.querySelectorAll('.fade-in-left, .fade-in-right');

//     const observer = new IntersectionObserver((entries) => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 entry.target.classList.add('in-view');
//                 observer.unobserve(entry.target); // Remove if you want to re-animate on scroll
//             }
//         });
//     }, {
//         threshold: 1
//     });

//     elements.forEach(el => observer.observe(el));
// });


document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.fade-in-left, .fade-in-right');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                observer.unobserve(entry.target); // Remove to re-trigger on scroll
            }
        });
    }, {
        threshold: 0.75, // Trigger when 75% of the element is visible
        rootMargin: '-100px 0px' // Trigger earlier when element is closer to the top
    });

    elements.forEach(el => observer.observe(el));
});
