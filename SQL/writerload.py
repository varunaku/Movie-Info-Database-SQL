import mysql.connector
import json

def get_writer_info(crew_json):
    try:
        crew_data = crew_json.replace('None', 'null').replace("'", "\"")
        #print(crew_data)
        crew_data = json.loads(crew_data)
        return [member for member in crew_data if member.get('department') == 'Writing']
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
cursor.execute("SELECT credit_id, gender, name, id, movie_id FROM Writer")
rows = cursor.fetchall() 
cursor.close()

#For each of the rows since we have fetched them all
for (credit_id, gender, name, writer_id, movie_id) in rows:
    #print("movie_id: " + movie_id)
    writers = get_writer_info(credit_id)  
    for writer in writers:
        wri_credit_id = writer.get('credit_id')
        wri_gender = writer.get('gender')
        wri_name = writer.get('name')
        wri_id = writer.get('id')

        if wri_gender == 0:
                wri_gender = 'Not disclosed'
        elif wri_gender == 1:
                wri_gender = 'Female'
        else:
                wri_gender = 'Male'
        # They all exist right?
        if wri_credit_id and wri_gender and wri_name and wri_id and movie_id:
            cursor = cnx.cursor()
            insert = ("INSERT INTO TheWriter " 
                      "(credit_id, gender, name, id, movie_id) " 
                      "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(insert, (wri_credit_id, wri_gender, wri_name, wri_id, movie_id))
            cnx.commit()
            cursor.close()
cnx.close()


