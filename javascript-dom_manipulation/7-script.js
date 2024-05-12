var moviesListElement = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => {
    if (!response.ok) {
      throw new Error(error);
    }
    return response.json();
  })
  .then(data => {
    data.results.forEach(movie => {
      var movieTitleElement = document.createElement("li");
      movieTitleElement.textContent = movie.title;
      moviesListElement.appendChild(movieTitleElement);
    });
  })
  .catch(error => {
    console.error(error);
  });
