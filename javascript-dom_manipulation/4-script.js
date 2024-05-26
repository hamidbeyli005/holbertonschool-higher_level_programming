const listClass = document.querySelector('.my_list');

const setItem = document.querySelector('#add_item');
setItem.addEventListener('click', () => {
  const new_item = document.createElement('li');
  new_item.textContent = 'Item';
  listClass.appendChild(new_item);
});
