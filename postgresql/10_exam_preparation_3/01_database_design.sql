CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE addresses(
    id SERIAL PRIMARY KEY,
    street_name VARCHAR(100) NOT NULL,
    street_number INT NOT NULL CHECK ( street_number > 0 ),
    town VARCHAR(30) NOT NULL,
    country VARCHAR(50) NOT NULL,
    zip_code INT NOT NULL CHECK ( zip_code > 0 )
);

CREATE TABLE publishers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    address_id INT REFERENCES addresses ON UPDATE CASCADE ON DELETE CASCADE NOT NULL,
    website VARCHAR(40),
    phone VARCHAR(20)
);

CREATE TABLE players_ranges(
    id SERIAL PRIMARY KEY,
    min_players INT NOT NULL CHECK ( min_players > 0 ),
    max_players INT NOT NULL CHECK ( max_players > 0 )
);

CREATE TABLE creators(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL
);

CREATE TABLE board_games(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    release_year INT NOT NULL CHECK ( release_year > 0 ),
    rating NUMERIC NOT NULL,
    category_id INT REFERENCES categories ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    publisher_id INT REFERENCES publishers ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    players_range_id INT REFERENCES players_ranges ON DELETE CASCADE ON UPDATE CASCADE NOT NULL

);

CREATE TABLE creators_board_games(
    creator_id INT REFERENCES creators ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    board_game_id INT REFERENCES board_games ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
);
