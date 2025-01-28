ALTER TABLE Distributor DROP FOREIGN KEY f_newmovieID;
ALTER TABLE HSXMaster DROP FOREIGN KEY fk_movieIDNew;
ALTER TABLE Producer DROP FOREIGN KEY fk_movieID8;
ALTER TABLE Writer DROP FOREIGN KEY fk_movieID7;
ALTER TABLE Director DROP FOREIGN KEY fk_movieID6;
ALTER TABLE Credit DROP FOREIGN KEY fk_movieID4;
ALTER TABLE Actor DROP FOREIGN KEY fk_movieID5;
DROP TABLE IF EXISTS TitleMapping;
DROP TABLE IF EXISTS HSXMaster;
DROP TABLE IF EXISTS Writer;
DROP TABLE IF EXISTS Actor;
DROP TABLE IF EXISTS NewCredit;
DROP TABLE IF EXISTS Credit;
DROP TABLE IF EXISTS Director;
DROP TABLE IF EXISTS Producer;
DROP TABLE IF EXISTS Distributor;

DROP TABLE IF EXISTS IDMapping2;
DROP TABLE IF EXISTS IDMapping4;
DROP TABLE IF EXISTS IDMapping5;
DROP TABLE IF EXISTS IDMapping6;
DROP TABLE IF EXISTS IDMapping7;


select '---------------------------------------------------------------------------------------' as '';

select 'Create Credit' as '';

create table Credit (
        cast text,
        crew text, 
        id int
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table Credit
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(cast, crew, id);

Create table NewCredit as (select id, MAX(cast) as cast, MAX(crew) as crew from Credit Group by id);

drop table Credit;

RENAME TABLE NewCredit TO Credit;

select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping2' as '';

CREATE TABLE IDMapping2 (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping2
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE Credit ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Credit C JOIN IDMapping2 I ON C.id = I.assign_id SET C.movie_imdb_id = I.imdb_id;

DELETE FROM Credit WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE Credit CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM Credit C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Credit ADD CONSTRAINT fk_movieID4 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);

select '---------------------------------------------------------------------------------------' as '';
select 'Create Actor' as '';
select '---------------------------------------------------------------------------------------' as '';
create table Actor (
        cast_id text,
        `character` text,
        credit_id text, 
        gender text,
        name text,
        id int
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table Actor
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(@cast, @crew, @id)
SET cast_id = @cast, `character` = @cast,  credit_id = @cast, gender = @cast, name = @cast, id=@id;

select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping4' as '';

CREATE TABLE IDMapping4 (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE Actor ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Actor C JOIN IDMapping4 I ON C.id = I.assign_id SET C.movie_imdb_id = I.imdb_id;

DELETE FROM Actor WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE Actor CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM Actor C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Actor ADD CONSTRAINT fk_movieID5 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);

select '+--------------------------------------------------------------------------------------' as '';
select '-' as '';
select 'Create Director' as '';
select '---------------------------------------------------------------------------------------' as '';
create table Director (
        credit_id varchar(5000), 
        gender varchar(5000),
        name varchar(5000),
        id int
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table Director
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(@cast, @crew, @id)
SET credit_id = @crew, gender = @crew, name = @crew, id=@id;

select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping5' as '';

CREATE TABLE IDMapping5 (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping5
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE Director ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Director C JOIN IDMapping5 I ON C.id = I.assign_id SET C.movie_imdb_id = I.imdb_id;

DELETE FROM Director WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE Director CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM Director C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Director ADD CONSTRAINT fk_movieID6 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);

select '-' as '';
select 'Create Writer' as '';
select '---------------------------------------------------------------------------------------' as '';
create table Writer (
        credit_id varchar(5000), 
        gender varchar(5000),
        name varchar(5000),
        id int
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table Writer
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(@cast, @crew, @id)
SET credit_id = @crew, gender = @crew, name = @crew, id=@id;

select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping6' as '';

CREATE TABLE IDMapping6 (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping6
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE Writer ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Writer C JOIN IDMapping6 I ON C.id = I.assign_id SET C.movie_imdb_id = I.imdb_id;

DELETE FROM Writer WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE Writer CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM Writer C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Writer ADD CONSTRAINT fk_movieID7 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);

select '-' as '';
select 'Create Producer' as '';
select '---------------------------------------------------------------------------------------' as '';
create table Producer (
        credit_id varchar(5000), 
        gender varchar(5000),
        name varchar(5000),
        id int
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/credits.csv' ignore into table Producer
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(@cast, @crew, @id)
SET credit_id = @crew, gender = @crew, name = @crew, id=@id;

select '---------------------------------------------------------------------------------------' as '';

select 'Create IDMapping7' as '';

CREATE TABLE IDMapping7 (
    assign_id int Primary key,
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE IDMapping7
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, assign_id, imdb_id, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE Producer ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE Producer C JOIN IDMapping7 I ON C.id = I.assign_id SET C.movie_imdb_id = I.imdb_id;

DELETE FROM Producer WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE Producer CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM Producer C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE Producer ADD CONSTRAINT fk_movieID8 FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);


select '---------------------------------------------------------------------------------------' as '';

select 'Create HSXMaster' as '';

create table HSXMaster (
        identifier char(5),
        title varchar(200) Not Null,
        status varchar(20),
        genres char(25),
        url varchar(75),
        ipo_date char(50),
        delist_date char(50),
        updated_at char(50)

        -- We still need to deal with foreign key mapping.
     );

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/hsx_bomojo_data/hsx_movie_master.csv' ignore into table HSXMaster
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
     ignore 1 lines
(identifier, title, @synopsis, status, @phase, genres, url, ipo_date, @release_date, delist_date, @mpaa_rating, @theaters, @distributor, @release_pattern, @domestic_gross, updated_at);

Create table NewHSXMaster as (select title, MAX(identifier) as identifier, MAX(status) as status, MAX(genres) as genres, MAX(url) as url, MAX(ipo_date) as ipo_date, MAX(delist_date) as delist_date, MAX(updated_at) as updated_at from HSXMaster Group by title);

drop table HSXMaster;

RENAME TABLE NewHSXMaster TO HSXMaster;

select 'Create TitleMapping' as '';

CREATE TABLE TitleMapping (
    original_title varchar(200),
    imdb_id VARCHAR(50) not null
);
LOAD DATA INFILE '/var/lib/mysql-files/03-Movies/movies_metadata.csv'
ignore INTO TABLE TitleMapping
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(@dummy, @dummy2, @dummy3, @dummy4, @dummy5, @dummy, imdb_id, @dummy6, original_title, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12, @dummy13, @dummy14, @dummy15, @dummy16, @dummy17, @dummy18, @dummy19, @dummy20, @dummy21);


ALTER TABLE HSXMaster ADD COLUMN movie_imdb_id VARCHAR(50);

UPDATE HSXMaster C JOIN TitleMapping I ON C.title = I.original_title SET C.movie_imdb_id = I.imdb_id;

DELETE FROM HSXMaster WHERE movie_imdb_id IS NULL;

-- ALTER TABLE Credit DROP COLUMN movie_id;

ALTER TABLE HSXMaster CHANGE movie_imdb_id movie_id VARCHAR(50);

DELETE C FROM HSXMaster C LEFT JOIN Movie M ON C.movie_id = M.movie_id WHERE M.movie_id IS NULL;

ALTER TABLE HSXMaster ADD CONSTRAINT fk_movieIDNew FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);

select '---------------------------------------------------------------------------------------' as '';

select 'Create Distributor' as '';

create table Distributor (
        movie_id varchar(50) primary key,
        distributor char(50)
	);

-- /var/lib/mysql-files/03-Movies/
load data infile '/var/lib/mysql-files/03-Movies/Mojo_budget_update.csv' ignore into table Distributor
     fields terminated by ','
     enclosed by '"'
     lines terminated by '\n'
(movie_id, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, distributor, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy, @dummy);

DELETE FROM Distributor WHERE movie_id NOT IN (SELECT movie_id FROM Movie);

ALTER TABLE Distributor ADD CONSTRAINT f_newmovieID FOREIGN KEY (movie_id) REFERENCES Movie(movie_id);



nowarning;
notee;