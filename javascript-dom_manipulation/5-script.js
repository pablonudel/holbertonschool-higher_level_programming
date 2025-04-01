const update_header = document.getElementById('update_header');
update_header.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.innerHTML = "New Header!!!"
})