--These are the tests we have run. Please see the report for more details regarding the testing

select * from TheActor limit 100;

SELECT COUNT(*) AS NumberOfRows FROM TheActor;

select * from TheDirector limit 100;

SELECT COUNT(*) AS NumberOfRows FROM TheDirector;

select * from Movie limit 3;

SELECT COUNT(*) AS NumberOfRows FROM Movie;

select * from HSXData limit 10;

select * from Distributor limit 10;

select * from Rating limit 10;

select * from Ticket limit 10;

select * from ExtraRevenues limit 10;

Select M.movie_id, M.movie_title, H.identifier, H.status, H.ipo_date, H.delist_date from Movie M LEFT JOIN HSXMaster H ON M.movie_id=H.movie_id WHERE H.ipo_date IS NOT NULL limit 10; 

Select table_name, column_name, constraint_name, referenced_table_name from information_schema.key_column_usage where referenced_table_schema = 'db356_team61' and referenced_table_name = 'Movie';

Select M.movie_id, M.movie_title, T.name from Movie M LEFT JOIN TheActor T ON M.movie_id=T.movie_id where T.name is not null limit 30;

select movie_id from MovieInfo where movie_id not in (select movie_id from Movie);

Select M.movie_id, M.movie_title, H.movie_year, H.mpaa from Movie M LEFT JOIN MovieInfo H ON M.movie_id=H.movie_id where H.movie_year is not null limit 10;