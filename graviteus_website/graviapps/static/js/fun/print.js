  const element = document.getElementById("typewriter");
  let i = 0;

  function typeWriter() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(typeWriter, 100);
    }
  }
  window.onload = typeWriter;