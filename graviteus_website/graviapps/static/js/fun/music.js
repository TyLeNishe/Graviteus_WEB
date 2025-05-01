const audio = document.getElementById('bgAudio');
const toggleBtn = document.getElementById('musicToggle');
let isPlaying = false;

audio.volume = 0.3;

toggleBtn.addEventListener('click', function() {
  if (isPlaying) {
    audio.pause();
    toggleBtn.textContent = 'Включить музыку';
  } else {
    audio.play();
    toggleBtn.textContent = 'Выключить музыку';
  }
  isPlaying = !isPlaying;
});