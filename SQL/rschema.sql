-- tee outfile2.txt;
-- warnings;
ALTER TABLE Director DROP FOREIGN KEY fk_movieID6;
ALTER TABLE Credit DROP FOREIGN KEY fk_movieID4;
ALTER TABLE Actor DROP FOREIGN KEY fk_movieID5;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS NewCredit;
DROP TABLE IF EXISTS Credit;
DROP TABLE IF EXISTS HSXMaster;
DROP TABLE IF EXISTS TempMovie;
DROP TABLE IF EXISTS TempMovie;
DROP TABLE IF EXISTS Distributor;
DROP TABLE IF EXISTS Director;
DROP TABLE IF EXISTS Rating;

ALTER TABLE Ticket DROP FOREIGN KEY f_year;
ALTER TABLE ExtraRevenues DROP FOREIGN KEY f_movieID2;
DROP TABLE IF EXISTS Year;
DROP TABLE IF EXISTS Ticket;
DROP TABLE IF EXISTS ExtraRevenues;
drop table if exists Rating;
Drop Table if exists MovieInfo;
-- DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS IDMapping;
DROP TABLE IF EXISTS IDMapping2;
DROP TABLE IF EXISTS IDMapping4;
DROP TABLE IF EXISTS IDMapping5;
Drop Table if exists TempYear;
Drop Table if exists MovieInfo;

-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Movie' as '';

-- create table Movie(
--         movie_id varchar(50) unique primary key,
--         movie_title varchar(200) Not Null,
--         adult char(10),
--         homepage varchar(500),
--         original_language char(10),
--         original_title varchar(200),
--         overview varchar(1000),
--         popularity decimal(15,10),
--         poster_path varchar(200),
--         movie_revenue int,
--         status varchar(25),
--         tagline varchar(255),
--         video char(10)
--         );

-- load data infile '/var/lib/mysql-files/03-Movies/movies_metadata.csv' ignore into table Movie
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (adult, @belongs_to_collection, @budget, @genres, homepage, @id, movie_id, original_language, original_title, overview, popularity, poster_path, @production_companies, @production_countries, @release_date, movie_revenue, @runtime, @spoken_languages, status, tagline, movie_title, video, @vote_average, @vote_count);

-- DELETE FROM Movie WHERE movie_title IS NULL OR movie_title = '' OR movie_id IS NULL OR movie_id = '';

select '---------------------------------------------------------------------------------------' as '';

select 'Create MovieInfo' as '';

create table MovieInfo (
        movie_id varchar(50),
        -- movie_title varchar(200) not null,
        movie_year int not null,
        trivia varchar(1200),
        mpaa char(50),
        release_date char(50),
        runtime char(50),
        budget int,
        html varchar(75),
        Primary key(movie_id)

	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table MovieInfo
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(movie_id, @dummy, movie_year, trivia, mpaa, release_date, runtime, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, budget, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, html);

DELETE FROM MovieInfo WHERE movie_id NOT IN (SELECT movie_id FROM Movie);
DELETE FROM MovieInfo WHERE movie_id = '';

ALTER TABLE MovieInfo ADD CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);



select '---------------------------------------------------------------------------------------' as '';

select 'Create ExtraRevenues' as '';

create table ExtraRevenues(
        movie_id varchar(50),
        domestic_revenue int,
        international_revenue int,
        worldwide_revenue int,
        PRIMARY KEY(movie_id)
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table ExtraRevenues
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(movie_id, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, domestic_revenue, international_revenue, worldwide_revenue, @dummy, @dummy, @dummy, @dummy);

DELETE FROM ExtraRevenues WHERE movie_id NOT IN (SELECT movie_id FROM Movie);

ALTER TABLE ExtraRevenues ADD CONSTRAINT f_movieID2 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);





select '---------------------------------------------------------------------------------------' as '';

select 'Create TempYear' as '';

CREATE TABLE TempYear (
    year INT NOT NULL PRIMARY KEY
);

load data infile '/var/lib/mysql-files/03-Movies/domestic_avg_movie_ticket_prices.csv' ignore into table TempYear
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(year, @dummy, @dummy);

select '---------------------------------------------------------------------------------------' as '';

select 'Create Year' as '';

CREATE TABLE Year (
    year INT NOT NULL PRIMARY KEY);

INSERT INTO Year (year) SELECT year FROM TempYear;

select '---------------------------------------------------------------------------------------' as '';

select 'Create Ticket' as '';

create table Ticket (
        ticketentry_id INT AUTO_INCREMENT PRIMARY KEY,
        year int not null,
        avg_movie_ticket_price_usd DECIMAL(10, 2) not null,
        source varchar(75),

        CONSTRAINT f_year FOREIGN KEY (year) REFERENCES Year(year)
        -- CONSTRAINT f_year FOREIGN KEY (year) REFERENCES Movie(movie_year)
	);
-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/domestic_avg_movie_ticket_prices.csv' ignore into table Ticket
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(year, avg_movie_ticket_price_usd, source);

DROP TABLE IF EXISTS TempYear;





select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping' as '';

CREATE TABLE IDMapping (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


select '---------------------------------------------------------------------------------------' as '';

select 'Create Rating' as '';

create table Rating (
        rating_id INT AUTO_INCREMENT,
        userId int,
        movie_id varchar(50),
        rating DECIMAL(2,1),
        timestamp int,
        PRIMARY KEY(rating_id)

        -- We still need to deal with foreign key mapping.
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/ratings_small.csv' ignore into table Rating
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(userId, movie_id, rating, timestamp);

ALTER TABLE Rating ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Rating R JOIN IDMapping M ON R.movie_id = M.assign_id SET R.movie_imdb_id = M.imdb_id;

DELETE FROM Rating WHERE movie_imdb_id IS NULL;

ALTER TABLE Rating DROP COLUMN movie_id;

ALTER TABLE Rating CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE R FROM Rating R LEFT JOIN Movie M ON R.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Rating ADD CONSTRAINT fk_movieID3 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);



-- TODO: 
-- Finish the other tables





-- nowarning;
-- notee;