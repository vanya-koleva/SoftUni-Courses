CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
    creator_name VARCHAR(30)
) RETURNS INT AS
$$
DECLARE
    games_count INT;
BEGIN
    SELECT
        COUNT(cbg.board_game_id)
    INTO
        games_count
    FROM
        creators AS c
    LEFT JOIN
        creators_board_games AS cbg
    ON
        c.id = cbg.creator_id
    WHERE
        c.first_name = creator_name
    GROUP BY
        c.first_name;

    RETURN games_count;
END;
$$
LANGUAGE plpgsql;
