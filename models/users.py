import psycopg2
from api.db_connect import conn, cur
from werkzeug.security import generate_password_hash, \
     check_password_hash

class User_model():

    def register_user(username, email, password):
		#  Add new user to users database

        #create a dictionary to hold data to be inserted into database
        data = dict(username = username, email = email, password = generate_password_hash(password))

        try:
            cur.execute("""INSERT INTO users (username, email, password, created_at) VALUES 
                    (%(username)s, %(email)s, %(password)s, current_timestamp)""", data)

            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print (error)

        return 'User created'

    def users():
        #  Add new user to users from db

        all_users = list()
                
        try:
            cur.execute("SELECT * FROM users")

        except (Exception, psycopg2.DatabaseError) as error:
            print (error)

        results = cur.fetchall()

        return results

    def user_id(username, password):
        #  return user id from users table       

        try:
            cur.execute("SELECT * FROM users")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        results = cur.fetchall()

        for result in results:

            if result[1] == username and check_password_hash(result[3]  , password):
                user_id = result[0]
                return user_id