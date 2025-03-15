document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('theme-toggle');

    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark');
        toggleButton.textContent = '🌙';
    }   else {
            toggleButton.textContent = '☀️';
        }

    toggleButton.addEventListener('click', function () {
        document.body.classList.toggle('dark');
        if (document.body.classList.contains('dark')) {
            localStorage.setItem('theme', 'dark');
            toggleButton.textContent = '🌙';
        } else {
            localStorage.setItem('theme', 'light');
            toggleButton.textContent = '☀️';
        }
        });
    });