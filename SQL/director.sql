-- DROP TABLE IF EXISTS TheDirector;
-- DONT UNCOMMENT PLS


select '---------------------------------------------------------------------------------------' as '';

select 'Create TheDirector' as '';


create table TheDirector (
        director_key INT AUTO_INCREMENT,
        credit_id varchar(500), 
        gender varchar(50),
        name varchar(50),
        id int,
        movie_id varchar(50),
        primary key(director_key, movie_id)
	);

ALTER TABLE TheDirector ADD CONSTRAINT fk_movie_id_director FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);
DELETE FROM TheDirector WHERE NOT EXISTS (SELECT 1 FROM Movie WHERE Movie.movie_id = TheDirector.movie_id);

-- DONT RUN THIS BOYS IT WORKS