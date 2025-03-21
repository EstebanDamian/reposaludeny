function showLoading() {
    document.getElementById('loading').style.display = 'block'; // Muestra la imagen de carga
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none'; // Oculta la imagen de carga
}

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            showLoading(); // Muestra la imagen de carga al enviar el formulario
        });
    }
});

const video = document.getElementById('video1');
const muteButton = document.getElementById('muteButton');

// Agregar un evento de clic al botón
muteButton.addEventListener('click', () => {
    // Alternar el estado de mute
    video.muted = !video.muted;

    // Cambiar el texto del botón según el estado actual
    if (video.muted) {
        muteButton.textContent = 'Unmute'; // Si está silenciado, cambiar a "Unmute"
    } else {
        muteButton.textContent = 'Mute'; // Si no está silenciado, cambiar a "Mute"
    }
});

$('#carouselExampleIndicators').carousel({
    interval: 1500 // 3000ms = 3 segundos
});

window.onload = function() {
    const btnFlotante = document.querySelector('.btn-flotante');
    const alturaPagina = document.body.scrollHeight; // Altura total de la página

    // Función para mover el botón hacia arriba
    function moverBoton() {
        let position = -100; // Comienza fuera de la vista
        const interval = setInterval(() => {
            if (position < alturaPagina) {
                position += 5; // Incrementa la posición hacia arriba
                btnFlotante.style.bottom = position + 'px'; // Mueve el botón
            } else {
                clearInterval(interval); // Detiene la animación al llegar al final
            }
        }, 10); // Intervalo de tiempo para la animación
    }

    moverBoton(); // Llama a la función para mover el botón
};

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("currentYear").textContent = new Date().getFullYear();
}); 


src="script.js"
function showLoading(event) {
    event.preventDefault(); // Evita el envío inmediato del formulario
    document.getElementById('loading').style.display = 'block';
    
    // Simula un tiempo de carga de 2 segundos
    setTimeout(() => {
        document.querySelector('form').submit(); // Envía el formulario
    }, 2000);
}
    
