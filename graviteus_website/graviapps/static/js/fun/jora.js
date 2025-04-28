document.addEventListener('DOMContentLoaded', () => {
    const spawnableElements = document.querySelectorAll('.spawnable');
    let spawnChance = 25; // Шанс спавна

    function spawnBlackRectangle() {
        if (Math.random() * 100 <= spawnChance) {
            const randomElement = spawnableElements[Math.floor(Math.random() * spawnableElements.length)];

            if (!randomElement.querySelector('.jora')) {
                const smallBlack = document.createElement('div');
                smallBlack.classList.add('jora');
                smallBlack.style.zIndex = '999';

                const maxLeft = randomElement.offsetWidth - 50;
                const randomLeft = Math.random() * maxLeft;
                smallBlack.style.left = `${randomLeft}px`;

                smallBlack.addEventListener('click', (e) => {
                    e.stopPropagation();
                    randomElement.removeChild(smallBlack);
                });

                randomElement.appendChild(smallBlack);
            }
        }
    }

    setInterval(spawnBlackRectangle, 5000); //время 1 тика
});