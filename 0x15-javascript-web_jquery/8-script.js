const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, textStatus, jqXHR) {
  data.results.forEach(film => {
    $('#list_movies').append('<li>' + film.title + '</li>');
  });
});
