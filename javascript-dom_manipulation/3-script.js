const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', function () {
  const nextClass = header.classList.contains('red') ? 'green' : 'red';
  header.classList.remove('red', 'green');
  header.classList.add(nextClass);
});
