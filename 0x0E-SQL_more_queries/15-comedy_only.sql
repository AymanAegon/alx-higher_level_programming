-- lists all Comedy shows in the database hbtn_0d_tvshows

SELECT ts.title AS title FROM tv_shows ts, tv_show_genres tsg, tv_genres tg
where tg.name = 'Comedy' AND tg.id = tsg.genre_id AND tsg.show_id = ts.id
ORDER BY ts.title;
