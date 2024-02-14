-- A script that displays the top 3 of cities temperature during July & August
-- ordered by temperature (descending)
SELECT city, AVG((temperature - 32) / 1.8) AS avg_temp
FROM top_city
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
