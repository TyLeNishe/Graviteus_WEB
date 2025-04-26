document.addEventListener('DOMContentLoaded', () => {
    const container = document.createElement('div');
    container.className = 'hacker-bg-container';
    document.body.appendChild(container);

    const createLayer = (zIndex, density = 1) => {
        const layer = document.createElement('div');
        layer.className = 'hacker-bg-layer';
        layer.style.zIndex = zIndex;
        container.appendChild(layer);

        const computedStyle = getComputedStyle(document.documentElement);
        const symbolsCount = parseInt(computedStyle.getPropertyValue('--hacker-bg-symbols-count')) || Math.floor(100 * density);
        const fallDuration = computedStyle.getPropertyValue('--hacker-bg-fall-duration') || '10s';
        const speedVariation = parseFloat(computedStyle.getPropertyValue('--hacker-bg-speed-variation')) || 0.5;

        const getRandomChar = () => String.fromCharCode(33 + Math.floor(Math.random() * 94));

        for (let i = 0; i < symbolsCount; i++) {
            const symbol = document.createElement('div');
            symbol.className = 'hacker-bg-symbol';
            symbol.textContent = getRandomChar();
            
            symbol.style.setProperty('--random-offset', Math.random());
            symbol.style.setProperty('--random-x', Math.random());
            symbol.style.setProperty('--initial-opacity', (0.1 + Math.random() * 0.4).toString());
            symbol.style.setProperty('--animation-delay', `${Math.random() * 3}s`);
            
            const durationVariation = 1 + (Math.random() * 2 - 1) * speedVariation;
            symbol.style.setProperty('--fall-duration', `calc(${fallDuration} * ${durationVariation})`);
            
            layer.appendChild(symbol);
        }
    };

    createLayer(-1, 0.8); 
    createLayer(-2, 1);   
});