// Карусель
const initCarousel = () => {
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    const btnPrev = document.querySelector('.prev');
    const btnNext = document.querySelector('.next');
  
    // Добавляем клоны слайдов для бесшовной прокрутки
    const firstClone = slides[0].cloneNode(true);
    const lastClone = slides[slides.length - 1].cloneNode(true);
    
    slider.appendChild(firstClone);
    slider.insertBefore(lastClone, slides[0]);
  
    let currentIndex = 1;
    let isAnimating = false;
    const totalSlides = slides.length + 2; 
  
    const updateSlider = () => {
      slider.style.transform = `translateX(-${currentIndex * 50}%)`;
    };
  
    const handleTransitionEnd = () => {
      isAnimating = false;
      
      if (currentIndex === 0) {
        currentIndex = totalSlides - 2;
        slider.style.transition = 'none';
        updateSlider();
        setTimeout(() => {
          slider.style.transition = 'transform 0.5s ease-in-out';
        }, 20);
      } else if (currentIndex === totalSlides - 1) {
        currentIndex = 1;
        slider.style.transition = 'none';
        updateSlider();
        setTimeout(() => {
          slider.style.transition = 'transform 0.5s ease-in-out';
        }, 20);
      }
    };
  
    const goNext = () => {
      if (isAnimating) return;
      isAnimating = true;
      currentIndex++;
      slider.style.transition = 'transform 0.5s ease-in-out';
      updateSlider();
    };
  
    const goPrev = () => {
      if (isAnimating) return;
      isAnimating = true;
      currentIndex--;
      slider.style.transition = 'transform 0.5s ease-in-out';
      updateSlider();
    };
  
    let touchStartX = 0;
    let touchEndX = 0;
  
    const handleTouchStart = (e) => {
      touchStartX = e.changedTouches[0].screenX;
    };
  
    const handleTouchEnd = (e) => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchEndX < touchStartX - 50) goNext(); 
      if (touchEndX > touchStartX + 50) goPrev(); 
    };
  
    btnNext.addEventListener('click', goNext);
    btnPrev.addEventListener('click', goPrev);
    slider.addEventListener('transitionend', handleTransitionEnd);
    slider.addEventListener('touchstart', handleTouchStart, { passive: true });
    slider.addEventListener('touchend', handleTouchEnd, { passive: true });
  
    slider.style.transform = `translateX(-${currentIndex * 50}%)`;
  };
  
  const initScrollEffect = () => {
    const body = document.body;
    const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    const colorStops = [
      { pos: 0.0, color: [35, 40, 62] },
      { pos: 0.5, color: [0, 0, 0] },
      { pos: 1.0, color: [87, 41, 43] }
    ];
  
    const interpolateColor = (progress) => {
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
    };
  
    const handleScroll = () => {
      const scrollProgress = Math.min(1, Math.max(0, window.pageYOffset / maxScroll));
      const [r, g, b] = interpolateColor(scrollProgress);
      body.style.backgroundColor = `rgb(${r},${g},${b})`;
      body.style.transition = 'background-color 0.3s ease';
    };
  
    window.addEventListener('scroll', handleScroll);
    handleScroll();
  };
  
  document.addEventListener('DOMContentLoaded', () => {
    initCarousel();
    initScrollEffect();
  });