-- A script that displays the max temperature of each state
-- (ordered by State name).
SELECT state, MAX(temperature) AS max_temp
FROM your_table_name
GROUP BY state
ORDER BY state;
