-- DROP TABLE IF EXISTS TheProducer;
-- DONT UNCOMMENT PLS

-- Don't run again boys pls
select '---------------------------------------------------------------------------------------' as '';

select 'Create TheProducer' as '';


create table TheProducer (
        producer_key INT AUTO_INCREMENT,
        credit_id varchar(500), 
        gender varchar(50),
        name varchar(50),
        id int,
        movie_id varchar(50),
        primary key(producer_key, movie_id)
	);

ALTER TABLE TheProducer ADD CONSTRAINT fk_movie_id_producer FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);
DELETE FROM TheProducer WHERE NOT EXISTS (SELECT 1 FROM Movie WHERE Movie.movie_id = TheProducer.movie_id);
