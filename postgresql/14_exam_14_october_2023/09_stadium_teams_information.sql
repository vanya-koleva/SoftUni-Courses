CREATE OR REPLACE FUNCTION fn_stadium_team_name(
    stadium_name VARCHAR(30)
) RETURNS TABLE(
    teams_names VARCHAR
) AS
$$
BEGIN
    RETURN QUERY
    SELECT
        t.name
    FROM
        stadiums AS s
    JOIN
        teams AS t
    ON
        s.id = t.stadium_id
    WHERE
        s.name = stadium_name
    ORDER BY
        t.name
    ;
END;
$$
LANGUAGE plpgsql;
