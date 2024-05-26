const header = document.querySelector('header');

const setHeader = document.querySelector('#update_header');
setHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
