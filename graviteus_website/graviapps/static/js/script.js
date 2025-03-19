const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slide');
const btnPrev = document.querySelector('.prev');
const btnNext = document.querySelector('.next');

let currentIndex = 1;
let isAnimating = false;
const totalSlides = slides.length;

function updateSlider() {
    slider.style.transform = `translateX(-${currentIndex * 50}%)`;
}

function handleTransitionEnd() {
    isAnimating = false;

    if (currentIndex === 0) {
        currentIndex = totalSlides - 2;
        slider.style.transition = 'none';
        updateSlider();
        setTimeout(() => slider.style.transition = 'transform 0.5s ease-in-out');
    } else if (currentIndex === totalSlides - 1) {
        currentIndex = 1;
        slider.style.transition = 'none';
        updateSlider();
        setTimeout(() => slider.style.transition = 'transform 0.5s ease-in-out');
    }
}

btnNext.addEventListener('click', () => {
    if (isAnimating) return;
    isAnimating = true;
    currentIndex++;
    slider.style.transition = 'transform 0.5s ease-in-out';
    updateSlider();
});

btnPrev.addEventListener('click', () => {
    if (isAnimating) return;
    isAnimating = true;
    currentIndex--;
    slider.style.transition = 'transform 0.5s ease-in-out';
    updateSlider();
});

slider.addEventListener('transitionend', handleTransitionEnd);
slider.style.transform = `translateX(-${currentIndex * 50}%)`;

const body = document.body;
const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
const colorStops = [
    { pos: 0.0, color: [35, 40, 62] },
    { pos: 0.5, color: [0, 0, 0] },
    { pos: 1.0, color: [87, 41, 43] }
];

function interpolateColor(progress) {
    for (let i = 1; i < colorStops.length; i++) {
        if (progress <= colorStops[i].pos) {
            const prev = colorStops[i - 1];
            const next = colorStops[i];
            const t = (progress - prev.pos) / (next.pos - prev.pos);

            return [
                Math.round(prev.color[0] + t * (next.color[0] - prev.color[0])),
                Math.round(prev.color[1] + t * (next.color[1] - prev.color[1])),
                Math.round(prev.color[2] + t * (next.color[2] - prev.color[2]))
            ];
        }
    }
    return colorStops[colorStops.length - 1].color;
}

window.addEventListener('scroll', () => {
    const scrollProgress = window.pageYOffset / maxScroll;
    const [r, g, b] = interpolateColor(scrollProgress);
    body.style.backgroundColor = `rgb(${r},${g},${b})`;
});