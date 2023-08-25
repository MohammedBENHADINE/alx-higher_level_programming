-- lists all Comdedy shows
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres on tv_shows.id=tv_show_genres.show_id
JOIN tv_genres on tv_show_genres.genre_id=tv_genres.id
WHERE tv_genres.name="Comedy"
ORDER BY tv_shows.title ASC;
