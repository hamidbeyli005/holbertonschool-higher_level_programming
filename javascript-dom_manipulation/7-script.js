const filmList = document.querySelector('#list_movies');

fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (let index = 0; index < data.results.length; index++) {
      const new_film = document.createElement('li');
      new_film.textContent = data.results[index].title;
      filmList.appendChild(new_film);
    }
  });
