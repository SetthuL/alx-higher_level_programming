-- A cript that displays the average temperature
-- (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG((temperature - 32) / 1.8) AS avg_temp
FROM your_table_name
GROUP BY city
ORDER BY avg_temp DESC;
