SELECT
    p.title,
    CASE
        WHEN pri.rating <= 3.5 THEN 'poor'
        WHEN pri.rating <= 8 THEN 'good'
        ELSE 'excellent'
    END AS rating,
    CASE
        WHEN pri.has_subtitles = TRUE THEN 'Bulgarian'
        ELSE 'N/A'
    END AS subtitles,
    COUNT(pa.actor_id) AS actors_count
FROM
    productions AS p
JOIN
    productions_info AS pri
ON
    p.production_info_id = pri.id
JOIN
    productions_actors AS pa
ON
    p.id = pa.production_id
GROUP BY
    title,
    rating,
    subtitles
ORDER BY
    rating,
    actors_count DESC,
    title
;
