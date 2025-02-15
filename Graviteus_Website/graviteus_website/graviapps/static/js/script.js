document.addEventListener("scroll", function() {
    let scrollPosition = window.scrollY;
    let maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    let scrollPercent = scrollPosition / maxScroll;

    // Вычисляем цвета для градиента
    let r1 = Math.round(0 + (255 * scrollPercent)); // от 0 до 255 (черный → красный)
    let g1 = Math.round(31 - (31 * scrollPercent)); // от 31 до 0 (синий → черный)
    let b1 = Math.round(63 - (63 * scrollPercent)); // от 63 до 0 (темно-синий → черный)

    let r2 = Math.round(0 + (120 * scrollPercent)); // от 0 до 120 (черный → оранжевый)
    let g2 = Math.round(0 + (60 * scrollPercent)); // от 0 до 60 (черный → светло-красный)
    let b2 = Math.round(0 - (0 * scrollPercent)); // от 0 до 0 (черный остается черным)

    let newBackground = `linear-gradient(to bottom, rgb(${r1},${g1},${b1}), rgb(${r2},${g2},${b2}))`;

    document.body.style.background = newBackground;
});