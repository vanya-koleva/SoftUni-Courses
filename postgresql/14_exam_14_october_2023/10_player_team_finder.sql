CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
) AS
$$
DECLARE
    f_name VARCHAR(50);
    l_name VARCHAR(50);
BEGIN
    f_name := SPLIT_PART(player_name, ' ', 1);
    l_name := SPLIT_PART(player_name, ' ', 2);

    SELECT
        t.name
    INTO
        team_name
    FROM
        players AS p
    JOIN
        teams AS t
    ON
        p.team_id = t.id
    WHERE
        p.first_name = f_name
            AND
        p.last_name = l_name
    ;

    IF team_name IS NULL THEN team_name := 'The player currently has no team';
    END IF;

END;
$$
LANGUAGE plpgsql;
