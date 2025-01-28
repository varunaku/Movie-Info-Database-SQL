import mysql.connector
import json

def get_director_info(crew_json):
    try:
        crew_data = crew_json.replace('None', 'null').replace("'", "\"")
        #print(crew_data)
        crew_data = json.loads(crew_data)
        return [member for member in crew_data if member.get('job') == 'Director']
    except json.JSONDecodeError as e:
        #print("Error", ":", e)
        return []


user_name = input("Enter your username: ")
password_name = input("Enter your password: ")

#https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
cnx = mysql.connector.connect(
    host='riku.shoshin.uwaterloo.ca',
    user=user_name,  
    password=password_name, 
    database='db356_team61'  
)

cursor = cnx.cursor()
cursor.execute("SELECT credit_id, gender, name, id, movie_id FROM Director")
rows = cursor.fetchall() 
cursor.close()

#For each of the rows since we have fetched them all
for (credit_id, gender, name, director_id, movie_id) in rows:
    #print("movie_id: " + movie_id)
    directors = get_director_info(credit_id)  
    for director in directors:
        dir_credit_id = director.get('credit_id')
        dir_gender = director.get('gender')
        dir_name = director.get('name')
        dir_id = director.get('id')

        if dir_gender == 0:
                dir_gender = 'Not disclosed'
        elif dir_gender == 1:
                dir_gender = 'Female'
        else:
                dir_gender = 'Male'
        # They all exist right?
        if dir_credit_id and dir_gender and dir_name and dir_id and movie_id:
            cursor = cnx.cursor()
            insert = ("INSERT INTO TheDirector " 
                      "(credit_id, gender, name, id, movie_id) " 
                      "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(insert, (dir_credit_id, dir_gender, dir_name, dir_id, movie_id))
            cnx.commit()
            cursor.close()
cnx.close()


