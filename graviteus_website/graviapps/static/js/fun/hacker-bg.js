document.addEventListener('DOMContentLoaded', () => {
    const createLayer = (zIndex, scale, speedFactor) => {
        const layer = document.createElement('div');
        layer.className = `hacker-bg-layer`;
        document.body.appendChild(layer);

        const symbolsCount = parseInt(getComputedStyle(document.documentElement)
            .getPropertyValue('--hacker-bg-symbols-count'));
        const speedMin = parseFloat(getComputedStyle(document.documentElement)
            .getPropertyValue('--hacker-bg-speed-min'));
        const speedMax = parseFloat(getComputedStyle(document.documentElement)
            .getPropertyValue('--hacker-bg-speed-max'));

        for (let i = 0; i < symbolsCount; i++) {
            const symbol = document.createElement('div');
            symbol.className = 'hacker-bg-symbol';
            symbol.textContent = String.fromCharCode(33 + Math.random() * 94);
            symbol.style.left = `${Math.random() * 100}%`;
            symbol.style.animationDuration = `${speedMin + Math.random() * (speedMax - speedMin)}s`;
            symbol.style.opacity = `${0.1 + Math.random() * 0.5}`;
            layer.appendChild(symbol);
        }

        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            layer.style.transform = `translateY(${scrollY * speedFactor}px) translateZ(-${zIndex}px) scale(${scale})`;
        });
    };

    createLayer(1, 2, 0.3); 
    createLayer(2, 3, 0.2); 
});