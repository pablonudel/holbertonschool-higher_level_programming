async function getFilms() {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json()
        if (data && data.results) {
            return data.results;
        } else {
            throw new Error('Data not found');
        }
    } catch (err) {
        console.error(err);
    }
}

const listMovies = document.querySelector('#list_movies');
getFilms().then((movies) => {
    const movieItems = movies.map((movie) => `<li>${movie.title}</li>`).join('');
    listMovies.innerHTML = movieItems;
})