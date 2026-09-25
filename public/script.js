// Fetch movie data from the FastAPI backend
fetch("http://localhost:5000/api/movies")
//Convert the response into JSON and get the movie data
.then(response=>response.json())
.then( movies =>{
   // Find the movie row in the HTML
     const movieRow = document.getElementById("movie-row");
     // Create a card for each movie
     movies.forEach(movie => {
        const card=document.createElement("div");
        // Create an image element for the movie
        const image=document.createElement("img")
        // Set the movie image URL
        image.src=movie.image_url;
        // Create a title element for the movie
        const title=document.createElement("h3")
        // Set the movie title
        title.textContent = movie.title;
      // Add image and title to the movie card
        card.appendChild(image);
        card.appendChild(title);
        // Add the movie card to the movie row
        movieRow.appendChild(card);

     });

})