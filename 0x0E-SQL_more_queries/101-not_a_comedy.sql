-- lists all shows without the genre Comedy in the database
SELECT DISTINCT tv_shows.title FROM tv_shows
LEFT JOIN tv_show_genres on tv_shows.id=tv_show_genres.show_id
LEFT JOIN tv_genres on tv_show_genres.genre_id=tv_genres.id
WHERE NOT tv_genres.name="Comedy"
ORDER BY tv_shows.title ASC;
