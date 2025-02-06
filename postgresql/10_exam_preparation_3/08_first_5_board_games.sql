SELECT
    b.name,
    b.rating,
    c.name AS category_name
FROM
    board_games AS b
JOIN
    categories AS c
ON
    b.category_id = c.id
WHERE
    (b.rating > 7 AND b.name ILIKE '%a%')
        OR
    (b.rating > 7.5 AND (
        SELECT
            min_players + max_players
        FROM
            players_ranges AS pr
        WHERE
            pr.id = b.players_range_id
        ) BETWEEN 2 AND 5)
ORDER BY
    b.name,
    b.rating DESC
LIMIT 5
;
