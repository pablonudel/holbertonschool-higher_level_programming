const updateHeader = document.getElementById('update_header');
updateHeader.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.innerHTML = "New Header!!!"
})