UPDATE
    players_ranges
SET
    max_players = max_players + 1
WHERE
    id IN (
        SELECT
            pr.id
        FROM
            players_ranges AS pr
        JOIN
            board_games AS bg
        ON
            pr.id = bg.players_range_id
        WHERE
            pr.min_players = 2
                AND
            pr.max_players = 2
    )
;

UPDATE
    board_games
SET
    name = CONCAT(name, ' V2')
WHERE
    release_year >= 2020
;
