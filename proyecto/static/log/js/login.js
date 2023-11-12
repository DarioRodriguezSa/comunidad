document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('.user');
    const customCheck = document.getElementById('customCheck');
    const loginButton = document.querySelector('.btn-primary');

    customCheck.addEventListener('change', function () {
        if (customCheck.checked) {
            customCheck.nextElementSibling.textContent = 'Has marcado "Recordarme"';
        } else {
            customCheck.nextElementSibling.textContent = 'Recordarme';
        }
    });

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const username = loginForm.querySelector('#id_username').value;
        const password = loginForm.querySelector('#id_password').value;

        if (username === '' || password === '') {
            alert('Por favor, completa ambos campos de usuario y contraseña.');
        } else {
            alert('Inicio de sesión exitoso. Redirigiendo...');
            // Aquí puedes redirigir al usuario a la página de inicio, por ejemplo:
            // window.location.href = '/inicio/';
        }
    });
});