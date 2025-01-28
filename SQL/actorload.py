import mysql.connector
import json

def get_actor_info(cast_json):
    try:
        cast_data = cast_json.replace('None', 'null').replace("'", "\"")
        #print(cast_data)
        cast_data = json.loads(cast_data)
        return [member for member in cast_data]
    except json.JSONDecodeError as e:
        #print("Error", ":", e)
        return []

# Establish a connection to the database
user_name = input("Enter your username: ")
password_name = input("Enter your password: ")

cnx = mysql.connector.connect(
    host='riku.shoshin.uwaterloo.ca',
    user=user_name,
    password=password_name,
    database='db356_team61'
)

cursor = cnx.cursor()
cursor.execute("SELECT cast_id, gender, name, id, movie_id FROM Actor")
rows = cursor.fetchall() 
cursor.close()

#For each of the rows since we have fetched them all
for (cast_id, gender, name, actor_id, movie_id) in rows:
    #print("movie_id: " + movie_id)
    actors = get_actor_info(cast_id)  
    for actor in actors:
        cast_id = actor.get('cast_id')
        character = actor.get('character')
        act_credit_id = actor.get('credit_id')
        act_gender = actor.get('gender')
        act_name = actor.get('name')
        act_id = actor.get('id')

        if act_gender == 0:
                act_gender = 'Not disclosed'
        elif act_gender == 1:
                act_gender = 'Female'
        else:
                act_gender = 'Male'
        # They all exist right?
        if cast_id and character and act_credit_id and act_gender and act_name and act_id and movie_id:
            #print(act_credit_id, act_gender, act_name, act_id, movie_id)
            cursor = cnx.cursor()
            insert = ("INSERT INTO TheActor" 
                      "(cast_id, `character`, credit_id, gender, name, id, movie_id) " 
                      "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(insert, (cast_id, character, act_credit_id, act_gender, act_name, act_id, movie_id))
            cnx.commit()
            cursor.close()
cnx.close()
