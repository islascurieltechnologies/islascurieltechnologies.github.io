document.addEventListener("DOMContentLoaded", function () {
  const boton = document.getElementById("entrar");
  const audio = new Audio("entrada.mp3");

  boton.addEventListener("click", function () {
    audio.play();

    // Esperamos 1 segundo (1000 ms) para mostrar el contenido
    setTimeout(() => {
      document.getElementById("bienvenida").style.display = "none";
      document.getElementById("contenido").style.display = "block";
    }, 1000);
  });
});
