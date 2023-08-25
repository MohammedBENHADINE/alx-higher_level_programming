-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(tv_show_ratings.rate) as rating FROM tv_shows
JOIN tv_show_ratings on tv_shows.id=tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
