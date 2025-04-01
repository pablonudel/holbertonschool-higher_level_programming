const toggle_header = document.getElementById("toggle_header");
toggle_header.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.classList.toggle('green');
    header.classList.toggle('red');
});
