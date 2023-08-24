-- lists all cities contained in the database with a JOIN
SELECT cities.id, cities.name, states.name FROM cities
JOIN states on cities.state_id = states.id
ORDER BY cities.id
