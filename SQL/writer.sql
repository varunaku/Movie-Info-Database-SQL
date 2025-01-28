
select '---------------------------------------------------------------------------------------' as '';

select 'Create TheWriter' as '';


create table TheWriter (
        writer_key INT AUTO_INCREMENT,
        credit_id varchar(500), 
        gender varchar(50),
        name varchar(50),
        id int,
        movie_id varchar(50),
        primary key(writer_key, movie_id)
	);

ALTER TABLE TheWriter ADD CONSTRAINT fk_movie_id_writer FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);
DELETE FROM TheWriter WHERE NOT EXISTS (SELECT 1 FROM Movie WHERE Movie.movie_id = TheWriter.movie_id);
