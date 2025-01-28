import mysql.connector
from mysql.connector import Error
from getpass import getpass
import os
import re


def manual():
    print("\nWelcome to the manual! The following commands are currently supported:\n")

    print("  To query the database with your own sql code type 'sql' followed by the sql command (Ex. sql SELECT * FROM Movie;)\n")
    print("  To create a new entry in any table type 'create' followed by the appropriate flags")
    print("  To update any entry in any table type 'update' followed by the appropriate flags")
    print("  To search for any entry type 'search' followed by the appropriate flags:\n")
    
    print("   -d followed by the Table (Ex. -d TheActor) for create/updates")
    print("   -d followed by either Movie or Ticket (Ex. -d Movie) for search\n")
    
    print("------------------------------Flags for Movies------------------------------")
    print("    -mi followed by the IMDb identifier of the movie (Ex. -mi tt8579674)")
    print("    -mt followed by the name of the movie (Ex. -mt Inception)")
    print("    -a followed by the adult status of the movie (Ex. -a True)")
    print("    -hp followed by the homepage URL of the movie (Ex. -hp https://example.com)")
    print("    -ol followed by the original language of the movie (Ex. -ol English)")
    print("    -ot followed by the original title of the movie (Ex. -ot Original Title)")
    print("    -o followed by the overview of the movie (Ex. -o This is a movie about...)")
    print("    -p followed by the popularity of the movie (Ex. -p 8.5)")
    print("    -pp followed by the poster path of the movie (Ex. -pp /path/to/poster)")
    print("    -mr followed by the movie revenue (Ex. -mr 1000000)")
    print("    -s followed by the status of the movie (Ex. -s Released)")
    print("    -tag followed by the tagline of the movie (Ex. -tag Just when you thought it was safe...)")
    print("    -v followed by the video status of the movie (Ex. -v True)")
    print("    -my followed by the release year of the movie (Ex. -my 2020)")
    print("    -t followed by the trivia of the movie (Ex. -t Interesting fact...)")
    print("    -mpaa followed by the MPAA rating of the movie (Ex. -mpaa PG-13)")
    print("    -rd followed by the release date of the movie (Ex. -rd 2020-01-01)")
    print("    -rt followed by the runtime of the movie (Ex. -rt 120)")
    print("    -b followed by the budget of the movie (Ex. -b 50000000)")
    print("    -h followed by the HTML content of the movie (Ex. -h <html>...)")
    print("    -dr followed by the domestic revenue of the movie (Ex. -dr 30000000)")
    print("    -ir followed by the international revenue of the movie (Ex. -ir 50000000)")
    print("    -wr followed by the worldwide revenue of the movie (Ex. -wr 80000000)")
    print("    -iden followed by the identifier from HSXMaster (Ex. -iden 12345)")
    print("    -si followed by the IPO status from HSXMaster (Ex. -si Active)")
    print("    -g followed by the genres of the movie (Ex. -g Action, Adventure)")
    print("    -u followed by the URL from HSXMaster (Ex. -u https://example.com)")
    print("    -ipod followed by the IPO date from HSXMaster (Ex. -ipod 2020-01-01)")
    print("    -dd followed by the delist date from HSXMaster (Ex. -dd 2021-01-01)")
    print("    -ua followed by the last updated date (Ex. -ua 2021-01-02)")
    print("    -dk followed by the director key (Ex. -dk 123)")
    print("    -dci followed by the director credit ID (Ex. -dci 456)")
    print("    -dg followed by the directors gender (Ex. -dg Male)")
    print("    -dn followed by the directors name (Ex. -dn Christopher Nolan)")
    print("    -did followed by the directors ID (Ex. -did 789)")
    print("    -ak followed by the actor key (Ex. -ak 321)")
    print("    -cai followed by the cast ID (Ex. -cai 654)")
    print("    -ch followed by the character name (Ex. -ch Protagonist)")
    print("    -aci followed by the actor credit ID (Ex. -aci 987)")
    print("    -ag followed by the actors gender (Ex. -ag Female)")
    print("    -an followed by the actors name (Ex. -an Leonardo DiCaprio)")
    print("    -aid followed by the actors ID (Ex. -aid 789)")
    print("    -pk followed by the producer key (Ex. -pk 246)")
    print("    -pci followed by the producer credit ID (Ex. -pci 135)")
    print("    -pg followed by the producers gender (Ex. -pg Male)")
    print("    -pn followed by the producers name (Ex. -pn Emma Thomas)")
    print("    -pid followed by the producers ID (Ex. -pid 753)")
    print("    -wk followed by the writer key (Ex. -wk 864)")
    print("    -wci followed by the writer credit ID (Ex. -wci 951)")
    print("    -wg followed by the writers gender (Ex. -wg Female)")
    print("    -wn followed by the writers name (Ex. -wn Jonathan Nolan)")
    print("    -wid followed by the writers ID (Ex. -wid 357)")
    print("    -dst followed by the distributor (Ex. -dst Warner Bros)")
    print("    -ri followed by the rating ID (Ex. -ri 123)")
    print("    -ui followed by the user ID (Ex. -ui 456)")
    print("    -r followed by the rating (Ex. -r 8.7)")
    print("    -time followed by the timestamp (Ex. -time 2021-01-01 00:00:00)\n")
    
    print("------------------------------Flags for Tickets------------------------------")
    print("    -tei followed by the ticket entry ID (Ex. -tei 1001)")
    print("    -y followed by the year (Ex. -y 2021)")
    print("    -avg followed by the average movie ticket price in USD (Ex. -avg 12.50)")
    print("    -source followed by the source (Ex. -source Box Office)\n")

def search(
    database,
    movie_id=None,
    movie_title=None,
    adult=None,
    homepage=None,
    original_language=None,
    original_title=None,
    overview=None,
    popularity=None,
    poster_path=None,
    movie_revenue=None,
    status=None,
    tagline=None,
    video=None,
    movie_year=None,
    trivia=None,
    mpaa=None,
    release_date=None,
    runtime=None,
    budget=None,
    html=None,
    domestic_revenue=None,
    international_revenue=None,
    worldwide_revenue=None,
    identifier=None,
    ipo_status=None,
    genres=None,
    url=None,
    ipo_date=None,
    delist_date=None,
    updated_at=None,
    director_key=None,
    director_credit_id=None,
    director_gender=None,
    director_name=None,
    director_id=None,
    actor_key=None,
    cast_id=None,
    character=None,
    actor_credit_id=None,
    actor_gender=None,
    actor_name=None,
    actor_id=None,
    producer_key=None,
    producer_credit_id=None,
    producer_gender=None,
    producer_name=None,
    producer_id=None,
    writer_key=None,
    writer_credit_id=None,
    writer_gender=None,
    writer_name=None,
    writer_id=None,
    distributor=None,
    rating_id=None,
    userId=None,
    rating=None,
    timestamp=None,
    ticketentry_id=None,
    year=None,
    avg_movie_ticket_price_usd=None,
    source=None,
):
    conditions = []

    if database == "Movie":
        base_query = """
        SELECT DISTINCT Movie.*, MovieInfo.*, ExtraRevenues.*, HSXMaster.*, TheDirector.*, TheActor.*, TheProducer.*, TheWriter.*, Distributor.*, Rating.*
        FROM Movie
        LEFT JOIN MovieInfo ON Movie.movie_id = MovieInfo.movie_id
        LEFT JOIN ExtraRevenues ON Movie.movie_id = ExtraRevenues.movie_id
        LEFT JOIN HSXMaster ON Movie.movie_id = HSXMaster.movie_id
        LEFT JOIN Rating ON Movie.movie_id = Rating.movie_id
        LEFT JOIN TheDirector ON Movie.movie_id = TheDirector.movie_id
        LEFT JOIN TheActor ON Movie.movie_id = TheActor.movie_id
        LEFT JOIN TheProducer ON Movie.movie_id = TheProducer.movie_id
        LEFT JOIN TheWriter ON Movie.movie_id = TheWriter.movie_id
        LEFT JOIN Distributor ON Movie.movie_id = Distributor.movie_id
        """

        # Mapping of function arguments to database column names
        column_mapping = {
            "movie_id": "Movie.movie_id",
            "movie_title": "Movie.movie_title",
            "adult": "Movie.adult",
            "html": "MovieInfo.html",
            "original_language": "Movie.original_language",
            "original_title": "Movie.original_title",
            "popularity": "Movie.popularity",
            "poster_path": "Movie.poster_path",
            "overview": "Movie.overview",
            "movie_revenue": "Movie.movie_revenue",
            "status": "Movie.status",
            "tagline": "Movie.tagline",
            "video": "Movie.video",
            "movie_year": "MovieInfo.movie_year",
            "trivia": "MovieInfo.trivia",
            "mpaa": "MovieInfo.mpaa",
            "release_date": "MovieInfo.release_date",
            "runtime": "MovieInfo.runtime",
            "budget": "MovieInfo.budget",
            "rating_id": "Rating.rating_id",
            "userId": "Rating.userId",
            "rating": "Rating.rating",
            "timestamp": "Rating.timestamp",
            "domestic_revenue": "ExtraRevenues.domestic_revenue",
            "international_revenue": "ExtraRevenues.international_revenue",
            "worldwide_revenue": "ExtraRevenues.worldwide_revenue",
            "distributor": "Distributor.name",
            "director_key": "TheDirector.director_key",
            "director_credit_id": "TheDirector.credit_id",
            "director_gender": "TheDirector.gender",
            "director_name": "TheDirector.name",
            "director_id": "TheDirector.id",
            "producer_key": "TheProducer.producer_key",
            "producer_credit_id": "TheProducer.credit_id",
            "producer_gender": "TheProducer.gender",
            "producer_name": "TheProducer.name",
            "producer_id": "TheProducer.id",
            "writer_key": "TheWriter.writer_key",
            "writer_credit_id": "TheWriter.credit_id",
            "writer_gender": "TheWriter.gender",
            "writer_name": "TheWriter.name",
            "writer_id": "TheWriter.id",
            "actor_key": "TheActor.actor_key",
            "cast_id": "TheActor.cast_id",
            "character": "TheActor.`character`",  # Using double quotes to escape the reserved keyword
            "actor_credit_id": "TheActor.credit_id",
            "actor_gender": "TheActor.gender",
            "actor_name": "TheActor.name",
            "actor_id": "TheActor.id",
        }

    elif database == "Ticket":
        base_query = "SELECT * FROM Ticket"

        # Mapping of function arguments to database column names
        column_mapping = {
            "ticketentry_id": "Ticket.ticketentry_id",
            "year": "Ticket.year",
            "avg_movie_ticket_price_usd": "Ticket.avg_movie_ticket_price_usd",
            "source": "Ticket.source",
        }
    for key, value in column_mapping.items():
        if locals()[key] is not None:
            conditions.append(f"{value} LIKE '%{locals()[key]}%'")
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    base_query += ";"
    # print(base_query)
    execute_read_query(database, connection, base_query)


def create(
    database,
    movie_id=None,
    movie_title=None,
    adult=None,
    homepage=None,
    original_language=None,
    original_title=None,
    overview=None,
    popularity=None,
    poster_path=None,
    movie_revenue=None,
    status=None,
    tagline=None,
    video=None,
    movie_year=None,
    trivia=None,
    mpaa=None,
    release_date=None,
    runtime=None,
    budget=None,
    html=None,
    domestic_revenue=None,
    international_revenue=None,
    worldwide_revenue=None,
    identifier=None,
    ipo_status=None,
    genres=None,
    url=None,
    ipo_date=None,
    delist_date=None,
    updated_at=None,
    director_key=None,
    director_credit_id=None,
    director_gender=None,
    director_name=None,
    director_id=None,
    actor_key=None,
    cast_id=None,
    character=None,
    actor_credit_id=None,
    actor_gender=None,
    actor_name=None,
    actor_id=None,
    producer_key=None,
    producer_credit_id=None,
    producer_gender=None,
    producer_name=None,
    producer_id=None,
    writer_key=None,
    writer_credit_id=None,
    writer_gender=None,
    writer_name=None,
    writer_id=None,
    distributor=None,
    rating_id=None,
    userId=None,
    rating=None,
    timestamp=None,
    ticketentry_id=None,
    year=None,
    avg_movie_ticket_price_usd=None,
    source=None,
):
    columns = []
    values = []
    
    if database == 'Movie':
        if movie_id is not None:
            columns.append("movie_id")
            values.append(f"'{movie_id}'")
        if movie_title is not None:
            columns.append("movie_title")
            values.append(f"'{movie_title}'")
        if adult is not None:
            columns.append("adult")
            values.append(f"'{adult}'")
        if homepage is not None:
            columns.append("movie_id")
            values.append(f"'{movie_id}'")
        if original_language is not None:
            columns.append("original_language")
            values.append(f"'{original_language}'")
        if original_title is not None:
            columns.append("original_title")
            values.append(f"'{original_title}'")
        if overview is not None:
            columns.append("overview")
            values.append(f"'{overview}'")
        if popularity is not None:
            columns.append("popularity")
            values.append(f"'{popularity}'")
        if poster_path is not None:
            columns.append("poster_path")
            values.append(f"'{poster_path}'")
        if movie_revenue is not None:
            columns.append("movie_revenue")
            values.append(f"'{movie_revenue}'")
        if status is not None:
            columns.append("status")
            values.append(f"'{status}'")
        if tagline is not None:
            columns.append("tagline")
            values.append(f"'{tagline}'")   
        if video is not None:
            columns.append("video")
            values.append(f"'{video}'")   
    else:
        if movie_id is None:
            print("A valid Movie Id is needed to create entries in other tables")
            return
        else:
            if database == 'MovieInfo':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if movie_year is not None:
                    columns.append("movie_year")
                    values.append(f"'{movie_year}'")
                if mpaa is not None:
                    columns.append("mpaa")
                    values.append(f"'{mpaa}'")
                if release_date is not None:
                    columns.append("release_date")
                    values.append(f"'{release_date}'")
                if runtime is not None:
                    columns.append("runtime")
                    values.append(f"'{runtime}'")
                if html is not None:
                    columns.append("html")
                    values.append(f"'{html}'")
            elif database == 'ExtraRevenues':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if domestic_revenue is not None:
                    columns.append("domestic_revenue")
                    values.append(f"'{domestic_revenue}'")
                if international_revenue is not None:
                    columns.append("international_revenue")
                    values.append(f"'{international_revenue}'")
                if worldwide_revenue is not None:
                    columns.append("worldwide_revenue")
                    values.append(f"'{worldwide_revenue}'")
            elif database == 'TheDirector':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if director_key is not None:
                    columns.append("director_key")
                    values.append(f"'{director_key}'")
                if director_credit_id is not None:
                    columns.append("credit_id")
                    values.append(f"'{director_credit_id}'")
                if director_gender is not None:
                    columns.append("gender")
                    values.append(f"'{director_gender}'")
                if director_name is not None:
                    columns.append("name")
                    values.append(f"'{director_name}'")
                if director_id is not None:
                    columns.append("id")
                    values.append(f"'{director_id}'")
            elif database == 'TheActor':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if actor_key is not None:
                    columns.append("actor_key")
                    values.append(f"'{actor_key}'")
                if cast_id is not None:
                    columns.append("cast_id")
                    values.append(f"'{cast_id}'")
                if character is not None:
                    columns.append("`character`")
                    values.append(f"'{character}'")
                if actor_credit_id is not None:
                    columns.append("credit_id")
                    values.append(f"'{actor_credit_id}'")
                if actor_gender is not None:
                    columns.append("gender")
                    values.append(f"'{actor_gender}'")
                if actor_name is not None:
                    columns.append("name")
                    values.append(f"'{actor_name}'")
                if actor_id is not None:
                    columns.append("id")
                    values.append(f"'{actor_id}'")
            elif database == 'TheProducer':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if producer_key is not None:
                    columns.append("producer_key")
                    values.append(f"'{producer_key}'")
                if producer_credit_id is not None:
                    columns.append("credit_id")
                    values.append(f"'{producer_credit_id}'")
                if producer_gender is not None:
                    columns.append("gender")
                    values.append(f"'{producer_gender}'")
                if producer_name is not None:
                    columns.append("name")
                    values.append(f"'{producer_name}'")
                if producer_id is not None:
                    columns.append("id")
                    values.append(f"'{producer_id}'")
            elif database == 'TheWriter':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if writer_key is not None:
                    columns.append("writer_key")
                    values.append(f"'{writer_key}'")
                if writer_credit_id is not None:
                    columns.append("credit_id")
                    values.append(f"'{writer_credit_id}'")
                if writer_gender is not None:
                    columns.append("gender")
                    values.append(f"'{writer_gender}'")
                if writer_name is not None:
                    columns.append("name")
                    values.append(f"'{writer_name}'")
                if writer_id is not None:
                    columns.append("writer_id")
                    values.append(f"'{writer_id}'")
            elif database == 'Distributor':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if distributor is not None:
                    columns.append("distributor")
                    values.append(f"'{distributor}'")
            elif database == 'Rating':
                if movie_id is not None:
                    columns.append("movie_id")
                    values.append(f"'{movie_id}'")
                if rating_id is not None:
                    columns.append("rating_id")
                    values.append(f"'{rating_id}'")
                if userId is not None:
                    columns.append("userId")
                    values.append(f"'{userId}'")
                if rating is not None:
                    columns.append("rating")
                    values.append(f"'{rating}'")
                if timestamp is not None:
                    columns.append("timestamp")
                    values.append(f"'{timestamp}'")
            elif database == 'Ticket':
                if ticketentry_id is not None:
                    columns.append("ticketentry_id")
                    values.append(f"'{ticketentry_id}'")
                if year is not None:
                    columns.append("year")
                    values.append(f"'{year}'")
                if avg_movie_ticket_price_usd is not None:
                    columns.append("avg_movie_ticket_price_usd")
                    values.append(f"{avg_movie_ticket_price_usd}")
                if source is not None:
                    columns.append("source")
                    values.append(f"'{source}'")
           
    columns_str = ", ".join(columns)
    values_str = ", ".join(values)
    base_query = f"INSERT INTO {database} ({columns_str}) VALUES ({values_str});"
    # INSERT INTO TheActor (`character`, credit_id, gender, name, id, movie_id) VALUES ('big man2', 'newcreditid124', 'Gender', 'ak47', 123456, 'tt0303758');
    #print(base_query)
    execute_query(connection, base_query)
    
def update(
    database,
    movie_id=None,
    movie_title=None,
    adult=None,
    homepage=None,
    original_language=None,
    original_title=None,
    overview=None,
    popularity=None,
    poster_path=None,
    movie_revenue=None,
    status=None,
    tagline=None,
    video=None,
    movie_year=None,
    trivia=None,
    mpaa=None,
    release_date=None,
    runtime=None,
    budget=None,
    html=None,
    domestic_revenue=None,
    international_revenue=None,
    worldwide_revenue=None,
    identifier=None,
    ipo_status=None,
    genres=None,
    url=None,
    ipo_date=None,
    delist_date=None,
    updated_at=None,
    director_key=None,
    director_credit_id=None,
    director_gender=None,
    director_name=None,
    director_id=None,
    actor_key=None,
    cast_id=None,
    character=None,
    actor_credit_id=None,
    actor_gender=None,
    actor_name=None,
    actor_id=None,
    producer_key=None,
    producer_credit_id=None,
    producer_gender=None,
    producer_name=None,
    producer_id=None,
    writer_key=None,
    writer_credit_id=None,
    writer_gender=None,
    writer_name=None,
    writer_id=None,
    distributor=None,
    rating_id=None,
    userId=None,
    rating=None,
    timestamp=None,
    ticketentry_id=None,
    year=None,
    avg_movie_ticket_price_usd=None,
    source=None,
):
    update_statements = []

    if database == 'Movie':
        if movie_id is not None:
            update_statements.append(f"movie_id = '{movie_id}'")
        if movie_title is not None:
            update_statements.append(f"movie_title = '{movie_title}'")
        if adult is not None:
            update_statements.append(f"adult = '{adult}'")
        if homepage is not None:
            update_statements.append(f"homepage = '{homepage}'")
        if original_language is not None:
            update_statements.append(f"original_language = '{original_language}'")
        if original_title is not None:
            update_statements.append(f"original_title = '{original_title}'")
        if overview is not None:
            update_statements.append(f"overview = '{overview}'")
        if popularity is not None:
            update_statements.append(f"popularity = '{popularity}'")
        if poster_path is not None:
            update_statements.append(f"poster_path = '{poster_path}'")
        if movie_revenue is not None:
            update_statements.append(f"movie_revenue = '{movie_revenue}'")
        if status is not None:
            update_statements.append(f"status = '{status}'")
        if tagline is not None:
            update_statements.append(f"tagline = '{tagline}'")
        if video is not None:
            update_statements.append(f"video = '{video}'")   
    else:
        if movie_id is None:
            print("A valid Movie Id is needed to create entries in other tables")
            return
        else:
            if database == 'MovieInfo':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if movie_year is not None:
                    update_statements.append(f"movie_year = '{movie_year}'")
                if mpaa is not None:
                    update_statements.append(f"mpaa = '{mpaa}'")
                if release_date is not None:
                    update_statements.append(f"release_date = '{release_date}'")
                if runtime is not None:
                    update_statements.append(f"runtime = '{runtime}'")
                if html is not None:
                    update_statements.append(f"html = '{html}'")
            elif database == 'ExtraRevenues':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if domestic_revenue is not None:
                    update_statements.append(f"domestic_revenue = '{domestic_revenue}'")
                if international_revenue is not None:
                    update_statements.append(f"international_revenue = '{international_revenue}'")
                if worldwide_revenue is not None:
                    update_statements.append(f"worldwide_revenue = '{worldwide_revenue}'")
            elif database == 'TheDirector':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if director_key is not None:
                    update_statements.append(f"director_key = '{director_key}'")
                if director_credit_id is not None:
                    update_statements.append(f"credit_id = '{director_credit_id}'")
                if director_gender is not None:
                    update_statements.append(f"gender = '{director_gender}'")
                if director_name is not None:
                    update_statements.append(f"name = '{director_name}'")
                if director_id is not None:
                    update_statements.append(f"id = '{director_id}'")
            elif database == 'TheActor':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if actor_key is not None:
                    update_statements.append(f"actor_key = '{actor_key}'")
                if cast_id is not None:
                    update_statements.append(f"cast_id = '{cast_id}'")
                if character is not None:
                    update_statements.append(f"`character` = '{character}'")
                if actor_credit_id is not None:
                    update_statements.append(f"credit_id = '{actor_credit_id}'")
                if actor_gender is not None:
                    update_statements.append(f"gender = '{actor_gender}'")
                if actor_name is not None:
                    update_statements.append(f"name = '{actor_name}'")
                if actor_id is not None:
                    update_statements.append(f"id = '{actor_id}'")
            elif database == 'TheProducer':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if producer_key is not None:
                    update_statements.append(f"producer_key = '{producer_key}'")
                if producer_credit_id is not None:
                    update_statements.append(f"credit_id = '{producer_credit_id}'")
                if producer_gender is not None:
                    update_statements.append(f"gender = '{producer_gender}'")
                if producer_name is not None:
                    update_statements.append(f"name = '{producer_name}'")
                if producer_id is not None:
                    update_statements.append(f"id = '{producer_id}'")
            elif database == 'TheWriter':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if writer_key is not None:
                    update_statements.append(f"writer_key = '{writer_key}'")
                if writer_credit_id is not None:
                    update_statements.append(f"credit_id = '{writer_credit_id}'")
                if writer_gender is not None:
                    update_statements.append(f"gender = '{writer_gender}'")
                if writer_name is not None:
                    update_statements.append(f"name = '{writer_name}'")
                if writer_id is not None:
                    update_statements.append(f"id = '{writer_id}'")
            elif database == 'Distributor':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if distributor is not None:
                    update_statements.append(f"distributor = '{distributor}'")
            elif database == 'Rating':
                if movie_id is not None:
                    update_statements.append(f"movie_id = '{movie_id}'")
                if rating_id is not None:
                    update_statements.append(f"rating_id = '{rating_id}'")
                if userId is not None:
                    update_statements.append(f"userId = '{userId}'")
                if rating is not None:
                    update_statements.append(f"rating = '{rating}'")
                if timestamp is not None:
                    update_statements.append(f"timestamp = '{timestamp}'")
            elif database == 'Ticket':
                if ticketentry_id is not None:
                    update_statements.append(f"ticketentry_id = '{ticketentry_id}'")
                if year is not None:
                    update_statements.append(f"year = '{year}'")
                if avg_movie_ticket_price_usd is not None:
                    update_statements.append(f"avg_movie_ticket_price_usd = '{avg_movie_ticket_price_usd}'")
                if source is not None:
                    update_statements.append(f"source = '{source}'")
    update_str = ", ".join(update_statements)      
    base_query = f"UPDATE {database} SET {update_str} WHERE movie_id = '{movie_id}';"
    # UPDATE Movies SET movie_title = 'New Movie Title', release_date = '2023-01-01' WHERE movie_id = 'some_movie_id';
    execute_query(connection, base_query)


def create_server_connection(host_name, user_name, db_name):
    connection = None
    try:
        user_name = input("Please enter your MySQL username: ")
        user_password = getpass("Please enter your MySQL password: ")
        connection = mysql.connector.connect(
            host="riku.shoshin.uwaterloo.ca",
            user=user_name,
            passwd=user_password,
            database="db356_team61",
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
        create_server_connection(host_name, user_name, db_name)
    return connection


def print_info(entity, result):
    printed = set()
    if entity == "Movie":
        for movie in result:
            if len(result) == 0:
                print("Nothing matches your search in the database try again!")
            else:
                (
                    movie_id,
                    movie_title,
                    adult,
                    homepage,
                    original_language,
                    original_title,
                    overview,
                    popularity,
                    poster_path,
                    movie_revenue,
                    status,
                    tagline,
                    video,
                    id1,
                    movie_year,
                    trivia,
                    mpaa,
                    release_date,
                    runtime,
                    budget,
                    html,
                    id1,
                    domestic_revenue,
                    international_revenue,
                    worldwide_revenue,
                    title,
                    identifier,
                    status1,
                    genres,
                    url,
                    blank,
                    ipo_date,
                    delist_date,
                    # updated_at,
                    id2,
                    director_key,
                    director_credit_id,
                    director_gender,
                    director_name,
                    director_id,
                    id3,
                    actor_key,
                    cast_id,
                    character,
                    actor_credit_id,
                    actor_gender,
                    actor_name,
                    actor_id,
                    id4,
                    producer_key,
                    producer_credit_id,
                    producer_gender,
                    producer_name,
                    producer_id,
                    idk,
                    writer_key,
                    writer_credit_id,
                    writer_gender,
                    writer_name,
                    writer_id,
                    id5,
                    id6,
                    distributor,
                    rating_id,
                    user_id,
                    rating,
                    timestamp,
                    id7,
                ) = movie
                if movie_id not in printed:
                    if movie_id is not None:
                        printed.add(movie_id)
                        print(f"\nIMDb ID: {movie_id}")
                    if movie_title is not None:
                        print(f"Name: {movie_title}")
                    if adult is not None:
                        print(f"Is an Adult Film: {adult}")
                    if homepage is not None:
                        print(f"Home Page: {homepage}")
                    if original_language is not None:
                        print(f"Original Language: {original_language}")
                    if original_title is not None:
                        print(f"Original Title: {original_title}")
                    if overview is not None:
                        print(f"Overview: {overview}")
                    if popularity is not None:
                        print(f"Popularity: {popularity}")
                    if poster_path is not None:
                        print(f"Poster Path: {poster_path}")
                    if movie_revenue is not None:
                        print(f"Movie Revenue: {movie_revenue}")
                    if status is not None:
                        print(f"Status: {status}")
                    if tagline is not None:
                        print(f"Tagline: {tagline}")
                    if video is not None:
                        print(f"Video: {video}")
                    if movie_year is not None:
                        print(f"Movie Year: {movie_year}")
                    if trivia is not None:
                        print(f"Trivia: {trivia}")
                    if mpaa is not None:
                        print(f"MPAA Rating: {mpaa}")
                    if release_date is not None:
                        print(f"Release Date: {release_date}")
                    if runtime is not None:
                        print(f"Runtime: {runtime}")
                    if budget is not None:
                        print(f"Budget: {budget}")
                    if html is not None:
                        print(f"HTML Content: {html}")
                    if domestic_revenue is not None:
                        print(f"Domestic Revenue: {domestic_revenue}")
                    if international_revenue is not None:
                        print(f"International Revenue: {international_revenue}")
                    if worldwide_revenue is not None:
                        print(f"Worldwide Revenue: {worldwide_revenue}")
                    if title is not None:
                        print(f"Distributor Title: {title}")
                    if identifier is not None:
                        print(f"Distributor Identifier: {identifier}")
                    if status1 is not None:
                        print(f"Distributor Status: {status1}")
                    if genres is not None:
                        print(f"Genres: {genres}")
                    if url is not None:
                        print(f"URL: {url}")
                    if blank is not None:
                        print(f"Blank Field: {blank}")
                    if ipo_date is not None:
                        print(f"IPO Date: {ipo_date}")
                    if delist_date is not None:
                        print(f"Delist Date: {delist_date}")
                    # Uncomment and use if necessary
                    # if updated_at is not None:
                    #     print(f"Updated At: {updated_at}")
                    if director_key is not None:
                        print(f"Director Key: {director_key}")
                    if director_credit_id is not None:
                        print(f"Director Credit ID: {director_credit_id}")
                    if director_gender is not None:
                        print(f"Director Gender: {director_gender}")
                    if director_name is not None:
                        print(f"Director Name: {director_name}")
                    if director_id is not None:
                        print(f"Director ID: {director_id}")
                    if actor_key is not None:
                        print(f"Actor Key: {actor_key}")
                    if cast_id is not None:
                        print(f"Cast ID: {cast_id}")
                    if character is not None:
                        print(f"Character: {character}")
                    if actor_credit_id is not None:
                        print(f"Actor Credit ID: {actor_credit_id}")
                    if actor_gender is not None:
                        print(f"Actor Gender: {actor_gender}")
                    if actor_name is not None:
                        print(f"Actor Name: {actor_name}")
                    if actor_id is not None:
                        print(f"Actor ID: {actor_id}")
                    if producer_key is not None:
                        print(f"Producer Key: {producer_key}")
                    if producer_credit_id is not None:
                        print(f"Producer Credit ID: {producer_credit_id}")
                    if producer_gender is not None:
                        print(f"Producer Gender: {producer_gender}")
                    if producer_name is not None:
                        print(f"Producer Name: {producer_name}")
                    if producer_id is not None:
                        print(f"Producer ID: {producer_id}")
                    if writer_key is not None:
                        print(f"Writer Key: {writer_key}")
                    if writer_credit_id is not None:
                        print(f"Writer Credit ID: {writer_credit_id}")
                    if writer_gender is not None:
                        print(f"Writer Gender: {writer_gender}")
                    if writer_name is not None:
                        print(f"Writer Name: {writer_name}")
                    if writer_id is not None:
                        print(f"Writer ID: {writer_id}")
                    if distributor is not None:
                        print(f"Distributor: {distributor}")
                    if rating_id is not None:
                        print(f"Rating ID: {rating_id}")
                    if user_id is not None:
                        print(f"User ID: {user_id}")
                    if rating is not None:
                        print(f"Rating: {rating}")
                    if timestamp is not None:
                        print(f"Timestamp: {timestamp}")

    elif entity == "Ticket":
        for ticket in result:
            if len(result) == 0:
                print("Nothing matches your search in the database try again!")
            else:
                (ticketentry_id, year, avg_movie_ticket_price_usd, source) = ticket
                print(f"Ticket Entry ID: {ticketentry_id}")
                print(f"Year: {year}")
                print(f"Average Movie Ticket Price (USD): {avg_movie_ticket_price_usd}")
                print(f"Information Source: {source}\n")


# Function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Function to execute a read query and fetch data
def execute_read_query(entity, connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        if entity == "sql":
            print(result)
        elif entity == "Movie":
            print_info(entity, result)
        elif entity == "Ticket":
            print_info(entity, result)
        else:
            return result
    except Error as err:
        print(f"Error: '{err}'")


# Connection credentials
host = "your_host"  # Usually localhost or an IP address
user = "your_username"
database = "your_database_name"

# Establishing the database connection
connection = create_server_connection(host, user, database)

os.system("clear")

print(
    "Welcome to IM_Db356!\nFor more information type 'help' and to exit at anytime type 'quit'"
)
while 1:
    command = input("What would you like to do today? ")

    if command == "help":
        manual()
    elif command == "quit":
        exit()
    elif command.startswith("sql"):
        sQuery = command[len("sql") :].strip()
        entity = "sql"
        execute_read_query(entity, connection, sQuery)
    elif command.startswith("search"):
        # SELECT * FROM Movie JOIN MovieInfo ON Movie.movie_id = MovieInfo.movie_id WHERE Movie.movie_year > 2000;

        sQuery = command[len("search") :].strip()
        # Define the flag patterns
        flags = {
            "-d": "database",
            "-mi": "movie_id",
            # From Movie
            "-mt": "movie_title",
            "-a": "adult",
            "-hp": "homepage",
            "-ol": "original_language",
            "-ot": "original_title",
            "-o": "overview",
            "-p": "popularity",
            "-pp": "poster_path",
            "-mr": "movie_revenue",
            "-s": "status",
            "-tag": "tagline",
            "-v": "video",
            # From MovieInfo
            "-my": "movie_year",
            "-t": "trivia",
            "-mpaa": "mpaa",
            "-rd": "release_date",
            "-rt": "runtime",
            "-b": "budget",
            "-h": "html",
            # From ExtraRevenues
            "-dr": "domestic_revenue",
            "-ir": "international_revenue",
            "-wr": "worldwide_revenue",
            # From HSXMaster
            "-iden": "identifier",
            "si": "ipo_status",
            "g": "genres",
            "u": "url",
            "ipod": "ipo_date",
            "dd": "delist_date",
            "ua": "updated_at",
            # From TheDirector
            "-dk": "director_key",
            "-dci": "director_credit_id",
            "-dg": "director_gender",
            "-dn": "director_name",
            "-did": "director_id",
            # From TheActor
            "-ak": "actor_key",
            "-cai": "cast_id",
            "ch": "character",
            "-aci": "actor_credit_id",
            "-ag": "actor_gender",
            "-an": "actor_name",
            "-aid": "actor_id",
            # From TheProducer
            "-pk": "producer_key",
            "-pci": "producer_credit_id",
            "-pg": "producer_gender",
            "-pn": "producer_name",
            "-pid": "producer_id",
            # From TheWriter
            "-wk": "writer_key",
            "-wci": "writer_credit_id",
            "-wg": "writer_gender",
            "-wn": "writer_name",
            "-wid": "writer_id",
            # From Distributor
            "-dst": "distributor",
            # From Rating
            "-ri": "rating_id",
            "-ui": "userId",
            "-r": "rating",
            "-time": "timestamp",
            # From Ticket
            "-tei": "ticketentry_id",
            "-y": "year",
            "-avg": "avg_movie_ticket_price_usd",
            "-source": "source",
        }

        # Initialize the search parameters dictionary
        search_params = {value: None for key, value in flags.items()}

        # Split the input string into parts
        parts = re.split(r" (?=-)", sQuery)

        # Process each part
        for part in parts:
            flag = part.split(" ", 1)[0]
            if flag in flags:
                # Extract the parameter value
                param_value = part[len(flag) :].strip().strip('"')
                search_params[flags[flag]] = param_value

        # Call the search function with the parameters
        if search_params["database"] not in ["Movie", "Ticket"]:
            print(
                "That is an invalid request. Please refer to the manual by typing 'help'"
            )
        else:
            search(**search_params)
    elif command.startswith("create"):
        sQuery = command[len("create") :].strip()
        # Define the flag patterns
        flags = {
            "-d": "database",
            "-mi": "movie_id",
            # From Movie
            "-mt": "movie_title",
            "-a": "adult",
            "-hp": "homepage",
            "-ol": "original_language",
            "-ot": "original_title",
            "-o": "overview",
            "-p": "popularity",
            "-pp": "poster_path",
            "-mr": "movie_revenue",
            "-s": "status",
            "-tag": "tagline",
            "-v": "video",
            # From MovieInfo
            "-my": "movie_year",
            "-t": "trivia",
            "-mpaa": "mpaa",
            "-rd": "release_date",
            "-rt": "runtime",
            "-b": "budget",
            "-h": "html",
            # From ExtraRevenues
            "-dr": "domestic_revenue",
            "-ir": "international_revenue",
            "-wr": "worldwide_revenue",
            # From HSXMaster
            "-iden": "identifier",
            "-si": "ipo_status",
            "-g": "genres",
            "-u": "url",
            "-ipod": "ipo_date",
            "-dd": "delist_date",
            "-ua": "updated_at",
            # From TheDirector
            "-dk": "director_key",
            "-dci": "director_credit_id",
            "-dg": "director_gender",
            "-dn": "director_name",
            "-did": "director_id",
            # From TheActor
            "-ak": "actor_key",
            "-cai": "cast_id",
            "-ch": "character",
            "-aci": "actor_credit_id",
            "-ag": "actor_gender",
            "-an": "actor_name",
            "-aid": "actor_id",
            # From TheProducer
            "-pk": "producer_key",
            "-pci": "producer_credit_id",
            "-pg": "producer_gender",
            "-pn": "producer_name",
            "-pid": "producer_id",
            # From TheWriter
            "-wk": "writer_key",
            "-wci": "writer_credit_id",
            "-wg": "writer_gender",
            "-wn": "writer_name",
            "-wid": "writer_id",
            # From Distributor
            "-dst": "distributor",
            # From Rating
            "-ri": "rating_id",
            "-ui": "userId",
            "-r": "rating",
            "-time": "timestamp",
            # From Ticket
            "-tei": "ticketentry_id",
            "-y": "year",
            "-avg": "avg_movie_ticket_price_usd",
            "-source": "source",
        }

        # Initialize the create parameters dictionary
        create_params = {value: None for key, value in flags.items()}

        # Split the input string into parts
        parts = re.split(r" (?=-)", sQuery)

        # Process each part
        for part in parts:
            flag = part.split(" ", 1)[0]
            if flag in flags:
                # Extract the parameter value
                param_value = part[len(flag) :].strip().strip('"')
                create_params[flags[flag]] = param_value

        # Call the create function with the parameters
        if create_params["database"] not in ["Movie", "MovieInfo", "ExtraRevenues","HSXMaster","TheDirector","TheActor","TheProducer","TheWriter","Distributor","Rating","Ticket"]:
            print(
                'That is an invalid database. Please pick from one of the following: ["Movie", "MovieInfo", "ExtraRevenues","HSXMaster","TheDirector","TheActor","TheProducer","TheWriter","Distributor","Rating","Ticket"]'
            )
        else:
            create(**create_params)
    elif command.startswith("update"):
        sQuery = command[len("update") :].strip()
        # Define the flag patterns
        flags = {
            "-d": "database",
            "-mi": "movie_id",
            # From Movie
            "-mt": "movie_title",
            "-a": "adult",
            "-hp": "homepage",
            "-ol": "original_language",
            "-ot": "original_title",
            "-o": "overview",
            "-p": "popularity",
            "-pp": "poster_path",
            "-mr": "movie_revenue",
            "-s": "status",
            "-tag": "tagline",
            "-v": "video",
            # From MovieInfo
            "-my": "movie_year",
            "-t": "trivia",
            "-mpaa": "mpaa",
            "-rd": "release_date",
            "-rt": "runtime",
            "-b": "budget",
            "-h": "html",
            # From ExtraRevenues
            "-dr": "domestic_revenue",
            "-ir": "international_revenue",
            "-wr": "worldwide_revenue",
            # From HSXMaster
            "-iden": "identifier",
            "-si": "ipo_status",
            "-g": "genres",
            "-u": "url",
            "-ipod": "ipo_date",
            "-dd": "delist_date",
            "-ua": "updated_at",
            # From TheDirector
            "-dk": "director_key",
            "-dci": "director_credit_id",
            "-dg": "director_gender",
            "-dn": "director_name",
            "-did": "director_id",
            # From TheActor
            "-ak": "actor_key",
            "-cai": "cast_id",
            "-ch": "character",
            "-aci": "actor_credit_id",
            "-ag": "actor_gender",
            "-an": "actor_name",
            "-aid": "actor_id",
            # From TheProducer
            "-pk": "producer_key",
            "-pci": "producer_credit_id",
            "-pg": "producer_gender",
            "-pn": "producer_name",
            "-pid": "producer_id",
            # From TheWriter
            "-wk": "writer_key",
            "-wci": "writer_credit_id",
            "-wg": "writer_gender",
            "-wn": "writer_name",
            "-wid": "writer_id",
            # From Distributor
            "-dst": "distributor",
            # From Rating
            "-ri": "rating_id",
            "-ui": "userId",
            "-r": "rating",
            "-time": "timestamp",
            # From Ticket
            "-tei": "ticketentry_id",
            "-y": "year",
            "-avg": "avg_movie_ticket_price_usd",
            "-source": "source",
        }

        # Initialize the update parameters dictionary
        update_params = {value: None for key, value in flags.items()}

        # Split the input string into parts
        parts = re.split(r" (?=-)", sQuery)

        # Process each part
        for part in parts:
            flag = part.split(" ", 1)[0]
            if flag in flags:
                # Extract the parameter value
                param_value = part[len(flag) :].strip().strip('"')
                update_params[flags[flag]] = param_value

        # Call the update function with the parameters
        if update_params["database"] not in ["Movie", "MovieInfo", "ExtraRevenues","HSXMaster","TheDirector","TheActor","TheProducer","TheWriter","Distributor","Rating","Ticket"]:
            print(
                'That is an invalid database. Please pick from one of the following: ["Movie", "MovieInfo", "ExtraRevenues","HSXMaster","TheDirector","TheActor","TheProducer","TheWriter","Distributor","Rating","Ticket"]'
            )
        else:
            update(**update_params)
    else:
        print("That is an invalid request. Please refer to the manual by typing 'help'")

# Example of how to use the execute_query function to perform an operation
# query = "INSERT INTO movies (movie_title, movie_year) VALUES ('Inception', 2010);"
# execute_query(connection, query)
