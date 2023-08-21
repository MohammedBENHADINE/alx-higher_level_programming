-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 'July' OR month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

