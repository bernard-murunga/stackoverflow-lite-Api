from api.db_connect import conn, cur
import psycopg2


def create_tables():
    """ 
    create tables in the database
    """
    create_users = """ CREATE TABLE IF NOT EXISTS users (
          id SERIAL NOT NULL PRIMARY KEY,
          username varchar(255) UNIQUE NOT NULL,
          email varchar(255) UNIQUE NOT NULL,
          password varchar(255) NOT NULL,
          created_at timestamp  
        )
        """
    

    create_questions = """ CREATE TABLE IF NOT EXISTS questions (
            question_id SERIAL NOT NULL PRIMARY KEY,
            user_id int NOT NULL,
            question_title varchar(100) UNIQUE NOT NULL,
            question_details varchar(255) UNIQUE NOT NULL,    
            created_at timestamp,
            updated_at timestamp
        )
        """

    create_answers = """CREATE TABLE IF NOT EXISTS answers (
            id SERIAL NOT NULL PRIMARY KEY,
            user_id int NOT NULL,
            question_id int NOT NULL,
            answer_details varchar(255) UNIQUE NOT NULL,
            preferred varchar(255),
            created_at timestamp 
        )
        """

    db_tables = [create_users , create_questions , create_answers ]
        
    try:
        for table in db_tables:
            cur.execute(table)
            conn.commit()
            print("Tables created.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)