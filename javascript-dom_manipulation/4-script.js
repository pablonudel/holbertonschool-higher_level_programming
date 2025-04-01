const addItem = document.getElementById('add_item');
addItem.addEventListener('click', () => {
    const list = document.querySelector('.my_list');
    const newLi = document.createElement('li');
    newLi.appendChild(document.createTextNode('Item'));
    list.appendChild(newLi);
})