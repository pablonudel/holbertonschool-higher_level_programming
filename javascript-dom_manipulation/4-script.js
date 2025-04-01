const add_item = document.getElementById('add_item');
add_item.addEventListener('click', () => {
    const list = document.querySelector('.my_list');
    const newLi = document.createElement('li');
    newLi.appendChild(document.createTextNode('Item'));
    list.appendChild(newLi);
})