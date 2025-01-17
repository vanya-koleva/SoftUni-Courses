SELECT
	peak_name,
	LEFT(peak_name, 4) AS positive_left,
	LEFT(peak_name, -4) AS negative_left    --All characters except the LAST 4
FROM
	peaks
;
