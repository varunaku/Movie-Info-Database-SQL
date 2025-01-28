-- DROP TABLE IF EXISTS TheActor;
-- DONT UNCOMMENT PLS

-- Don't run again pls
select '---------------------------------------------------------------------------------------' as '';

select 'Create TheActor' as '';

create table TheActor (
        actor_key INT AUTO_INCREMENT,
        cast_id varchar(50),
        `character` varchar(500),
        credit_id varchar(500), 
        gender varchar(50),
        name varchar(50),
        id int,
        movie_id varchar(50),
        primary key(actor_key, movie_id)
	);

ALTER TABLE TheActor ADD CONSTRAINT fk_movie_id_actor FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);
DELETE FROM TheActor WHERE NOT EXISTS (SELECT 1 FROM Movie WHERE Movie.movie_id = TheActor.movie_id);
