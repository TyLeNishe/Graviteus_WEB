document.addEventListener('DOMContentLoaded', () => {
    const container = document.createElement('div');
    container.className = 'ripple-container';
    document.body.appendChild(container);

    document.addEventListener('click', (e) => {
        const ripple = document.createElement('div');
        const size = parseInt(getComputedStyle(document.documentElement)
            .getPropertyValue('--click-effect-size'));
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${e.clientX - size/2}px`;
        ripple.style.top = `${e.clientY - size/2}px`;
        ripple.className = 'ripple';

        container.appendChild(ripple);

        ripple.addEventListener('animationend', () => ripple.remove());
    });
});