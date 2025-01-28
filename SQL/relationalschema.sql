 tee outfile.txt;
warnings;
DROP TABLE IF EXISTS TempMovie;
-- DROP TABLE IF EXISTS Distributor;
-- DROP TABLE IF EXISTS Director;
-- DROP TABLE IF EXISTS Rating;

ALTER TABLE Ticket DROP FOREIGN KEY f_year;
-- DROP TABLE IF EXISTS Year;
DROP TABLE IF EXISTS Ticket;
-- DROP TABLE IF EXISTS Revenue;
-- drop table if exists Rating;
DROP TABLE IF EXISTS Movie;
--DROP TABLE IF EXISTS IDMapping;

-- -- drop table if exists Tickets;

-- -- drop table if exists Genre;
-- -- drop table if exists Composer;
-- -- drop table if exists Distributor;
-- -- drop table if exists Producer;
-- -- drop table if exists Writer;
-- -- drop table if exists Actor;

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
DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS IDMapping;
Drop Table if exists TempYear;
Drop Table if exists MovieInfo;









-- DONT USE THIS FILE ANY MORE











-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Movie' as '';

-- create table Movie (
--         movie_id varchar(50) unique primary key,
--         movie_title varchar(200) not null,
--         movie_year int not null,
--         trivia varchar(255),
--         mpaa char(50),
--         release_date char(50),
--         runtime char(50),
--         budget int,
--         html varchar(75),

--         INDEX(movie_year),
--         INDEX(movie_id)
-- 	);

-- -- /var/lib/mysql-files/03-Movies/
-- load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table Movie
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (movie_id, movie_title, movie_year, trivia, mpaa, release_date, runtime, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, budget, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, html);


-- create table TempMovie(
--         adult char(10),
--         homepage varchar(75),
--         imdb_id varchar(50),
--         original_language char(10),
--         original_title varchar(200),
--         overview varchar(700),
--         popularity decimal(20,20),
--         poster_path varchar(200),
--         status varchar(25),
--         tagline varchar(255),
--         video char(10)
--         );

-- load data infile '/var/lib/mysql-files/03-Movies/movies_metadata.csv' ignore into table TempMovie
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (adult, @dummy, @dummy, @dummy, homepage, @dummy, imdb_id, original_language, original_title, overview, popularity, poster_path, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, status, tagline, @dummy, video, @dummy, @dummy);

-- alter table Movie
-- add column adult char(10),
-- add column homepage varchar(75),
-- add column imdb_id varchar(50),
-- add column original_language char(10),
-- add column original_title varchar(200),
-- add column overview varchar(700),
-- add column popularity decimal(8,5),
-- add column poster_path varchar(200),
-- add column status varchar(25),
-- add column tagline varchar(255),
-- add column video char(10);
-- update Movie M join TempMovie T ON M.movie_id = T.imdb_id 
-- set
-- M.adult = T.adult,
-- M.homepage = T.homepage,
-- M.original_language = T.original_language,
-- M.original_title = T.original_title,
-- M.overview = T.overview,
-- M.popularity = T.popularity,
-- M.poster_path = T.poster_path,
-- M.status = T.status,
-- M.tagline = T.tagline,
-- M.video = T.video;
-- alter table Movie drop column imdb_id;
-- drop table if exists TempMovie;

-- Fix this later, where's the mapping?




-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Revenue' as '';

-- create table Revenue (
--         movie_id varchar(50),
--         domestic_revenue int,
--         international_revenue int,
--         worldwide_revenue int,

--         PRIMARY KEY(movie_id),
--         CONSTRAINT f_movieID FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
-- 	);

-- -- /var/lib/mysql-files/03-Movies/
-- load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table Revenue
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (movie_id, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, domestic_revenue, international_revenue, worldwide_revenue, @dummy, @dummy, @dummy, @dummy);
-- -- SET domestic_revenue = IFNULL(NULLIF(@domestic_revenue,''), 0),
-- --     international_revenue = IFNULL(NULLIF(@international_revenue,''), 0),
-- --     worldwide_revenue = IFNULL(NULLIF(@worldwide_revenue,''), 0);
-- -- SET teamIDfor = IF(@teamIDfor = 'NA', NULL, @teamIDfor),


-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create TempYear' as '';

-- CREATE TABLE TempYear (
--     year INT NOT NULL PRIMARY KEY
-- );

-- load data infile '/var/lib/mysql-files/03-Movies/domestic_avg_movie_ticket_prices.csv' ignore into table TempYear
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
-- (year, @dummy, @dummy);




-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Year' as '';

-- CREATE TABLE Year (
--     year INT NOT NULL PRIMARY KEY);

-- INSERT INTO Year (year) SELECT year FROM TempYear;



-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Ticket' as '';

-- create table Ticket (
--         ticket_id INT AUTO_INCREMENT PRIMARY KEY,
--         year int not null,
--         avg_movie_ticket_price_usd DECIMAL(10, 2) not null,
--         source varchar(75),

--         CONSTRAINT f_year FOREIGN KEY (year) REFERENCES Year(year)
--         -- CONSTRAINT f_year FOREIGN KEY (year) REFERENCES Movie(movie_year)
-- 	);
-- -- /var/lib/mysql-files/03-Movies/
-- load data infile '/var/lib/mysql-files/03-Movies/domestic_avg_movie_ticket_prices.csv' ignore into table Ticket
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (year, avg_movie_ticket_price_usd, source);


-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create IDMapping' as '';

-- CREATE TABLE IDMapping (
--     assign_id int Primary key,
--     imdb_id VARCHAR(50) not null
-- );
-- LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
-- ignore INTO TABLE IDMapping
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- (@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Rating' as '';

-- create table Rating (
--         rating_id INT AUTO_INCREMENT,
--         userId int,
--         movie_id varchar(50),
--         rating DECIMAL(2,1),
--         timestamp int,
--         PRIMARY KEY(rating_id)

--         -- We still need to deal with foreign key mapping.
-- 	);

-- -- /var/lib/mysql-files/03-Movies/
-- load data infile '/var/lib/mysql-files/03-Movies/ratings_small.csv' ignore into table Rating
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
--      ignore 1 lines
-- (userId, movie_id, rating, timestamp);

-- ALTER TABLE Rating ADD COLUMN movie_imdb_id VARCHAR(50);

-- UPDATE Rating R JOIN IDMapping M ON R.movie_id = M.assign_id SET R.movie_imdb_id = M.imdb_id;

-- DELETE FROM Rating WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Rating DROP COLUMN movie_id;

-- ALTER TABLE Rating CHANGE movie_imdb_id movie_id VARCHAR(50);

-- DELETE R FROM Rating R LEFT JOIN Movie M ON R.movie_id = M.movie_id WHERE M.movie_id IS NULL;

-- ALTER TABLE Rating ADD CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);


-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Distributor' as '';

-- create table Distributor (
--         movie_id varchar(50) primary key,
--         distributor char(50),
--         CONSTRAINT f_movie2ID FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
-- 	);

-- -- /var/lib/mysql-files/03-Movies/
-- load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table Distributor
--      fields terminated by ','
--      enclosed by '"'
--      lines terminated by '\n'
-- (movie_id, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, distributor, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy);















-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create TempDirector' as '';

-- create table TempDirector (
--     crew varchar(255) 
-- );

-- load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table TempDirector
--         fields terminated by ','
--         enclosed by '"'
--         lines terminated by '\n'
-- ignore 1 lines
-- (@dummy, crew, @dummy);

-- select '---------------------------------------------------------------------------------------' as '';

-- select 'Create Director' as '';

-- create table Director (
--         credit_id VARCHAR(50) primary key,
--         name CHAR(50),
--         gender INT
-- 	);

-- insert into Director (credit_id, name, gender)
-- select JSON_UNQUOTE(JSON_EXTRACT(crew, '$.credit_id')), JSON_UNQUOTE(JSON_EXTRACT(crew, '$.name')), JSON_UNQUOTE(JSON_EXTRACT(crew, '$.gender'))
-- from TempDirector
-- where JSON_UNQUOTE(JSON_EXTRACT(crew, '$.job')) = 'Director';

-- drop table if exists TempDirector;

-- DROP TABLE IF EXISTS TempYear;
nowarning;
notee;


