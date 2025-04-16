document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.glitch-text');
    
    elements.forEach(el => {
        el.setAttribute('data-text', el.textContent);
    });
});