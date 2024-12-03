function movies(input) {
    const movies = [];
    const addMovieCommand = 'addMovie';
    const directedByCommand = 'directedBy';
    const onDateCommand = 'onDate';

    for (const command of input) {
        if (command.includes(addMovieCommand)) {
            const movie = {
                name: command.substring(addMovieCommand.length + 1),
            };
            movies.push(movie);
        } else if (command.includes(directedByCommand)) {
            const [movieName, director] = command.split(` ${directedByCommand} `);
            const movie = movies.find(movie => movie.name === movieName);

            if (movie) {
                movie.director = director;
            }
        } else if (command.includes(onDateCommand)) {
            const [movieName, date] = command.split(` ${onDateCommand} `);
            const movie = movies.find(movie => movie.name === movieName);

            if (movie) {
                movie.date = date;
            }
        }
    }

    movies
        .filter(movie => movie.director && movie.date)
        .forEach(movie => console.log(JSON.stringify(movie)));
}

movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen',
]);
