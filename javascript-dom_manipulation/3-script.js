const toggleHeader = document.getElementById("toggle_header");
toggleHeader.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.classList.toggle('green');
    header.classList.toggle('red');
});
