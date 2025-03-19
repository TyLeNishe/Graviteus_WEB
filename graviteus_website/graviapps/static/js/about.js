document.addEventListener('DOMContentLoaded', function () {
    const aboutButton = document.getElementById('about-btn');

    if (aboutButton) {
        aboutButton.addEventListener('click', function (event) {
            if (window.location.pathname === '/about/') {
                event.preventDefault();
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            }
        });
    }
});