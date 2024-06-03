let url = https://swapi.co/api/films/?format=json';
$.get(url, function (data, stat) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
