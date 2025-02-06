SELECT
    id,
    CONCAT(first_name, ' ', last_name) AS creator_name,
    email
FROM
    creators
WHERE
    id NOT IN (
        SELECT
            creator_id
        FROM
            creators_board_games
    )
ORDER BY
    creator_name
;

