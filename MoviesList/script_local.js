document.addEventListener("DOMContentLoaded", function () {
  const movieList = document.getElementById("movie-list");

  // Fetch movie data from JSON file
  fetch("movies.json")
    .then((response) => response.json())
    .then((movies) => {
      movies.forEach((movie) => {
        const movieCard = document.createElement("div");
        movieCard.classList.add("movie-card");

        // Create HTML structure for each movie
        movieCard.innerHTML = `
          <iframe src="${movie.iframe_link}" allowfullscreen></iframe>
          <h2>${movie.title}</h2>
          <p><strong>Release Date:</strong> ${movie.release_date}</p>
          <p><strong>Director:</strong> ${movie.director}</p>
          <p><strong>Genres:</strong> ${movie.genres.join(", ")}</p>
          <p>${movie.description}</p>
        `;

        // Append the movie card to the movie list
        movieList.appendChild(movieCard);
      });
    })
    .catch((error) => console.error("Error loading movies:", error));
});