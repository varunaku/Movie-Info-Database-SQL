import mysql.connector
import json

def get_producer_info(crew_json):
    try:
        crew_data = crew_json.replace('None', 'null').replace("'", "\"")
        #print(crew_data)
        crew_data = json.loads(crew_data)
        return [member for member in crew_data if member.get('job') == 'Producer']
    except json.JSONDecodeError as e:
        print("Error", ":", e)
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
cursor.execute("SELECT credit_id, gender, name, id, movie_id FROM Producer")
rows = cursor.fetchall() 
cursor.close()

#For each of the rows since we have fetched them all
for (credit_id, gender, name, producer_id, movie_id) in rows:
    #print("movie_id: " + movie_id)
    producers = get_producer_info(credit_id)  
    for producer in producers:
        prod_credit_id = producer.get('credit_id')
        prod_gender = producer.get('gender')
        prod_name = producer.get('name')
        prod_id = producer.get('id')

        if prod_gender == 0:
                prod_gender = 'Not disclosed'
        elif prod_gender == 1:
                prod_gender = 'Female'
        else:
                prod_gender = 'Male'
        # They all exist right?
        if prod_credit_id and prod_gender and prod_name and prod_id and movie_id:
            print(prod_credit_id, prod_gender, prod_name, prod_id, movie_id)
            cursor = cnx.cursor()
            insert = ("INSERT INTO TheProducer " 
                      "(credit_id, gender, name, id, movie_id) " 
                      "VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(insert, (prod_credit_id, prod_gender, prod_name, prod_id, movie_id))
            cnx.commit()
            cursor.close()
cnx.close()