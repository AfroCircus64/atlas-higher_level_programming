-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT b.title, a.genre_id 
FROM tv_show_genres a 
LEFT JOIN tv_shows b 
ON a.show_id = b.id 
ORDER BY b.title, a.genre_id ASC;
