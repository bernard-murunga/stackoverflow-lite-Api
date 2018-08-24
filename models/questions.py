import psycopg2
from api.db_connect import conn, cur

class Questions_model():    
    def __init__(self, question_title, question_details, user_id):
        self.question_title = question_title
        self.question_details = question_details
        self.user_id = user_id

    def get_questions():
        #  Get all questions from database

        all_questions = list()

        try:
            cur.execute("SELECT * FROM questions")
                                  
            
        except psycopg2.DatabaseError as error:
            print(error)

        
        results = cur.fetchall()

        for result in results:
            all_questions.append(dict(question_id = result[0] , user_id = result[1], question_title = result[2], question_detail = result[3]))
        
        return all_questions

    
    def insert_question(self):
        #  Insert questions title and details to questions table

        data = dict(user_id = self.user_id, question_title=self.question_title, question_details = self.question_details)

        try:
            cur.execute("""INSERT INTO questions (user_id, question_title, question_details, created_at) VALUES 
                    (%(user_id)s, %(question_title)s, %(question_details)s, current_timestamp )""", data)

            conn.commit()

            return "Successfully added question"

        except psycopg2.DatabaseError as error:
            print(error)

    def one_question():
        # Get questions

        all_questions = list()

        try:
            cur.execute("SELECT * FROM questions")
                                  
            
        except psycopg2.DatabaseError as error:
            print(error)

        results = cur.fetchall()

        for result in results:
            all_questions.append(dict(question_id = result[0] , user_id = result[1], question_title = result[2], question_detail = result[3]))

            
        return all_questions

    def del_question(question_id):
        #  Delete a question
        try:
            query = "DELETE FROM questions WHERE question_id = %s;"
            cur.execute(query, [question_id])
            conn.commit()

            return "Deletion successful"
        except psycopg2.DatabaseError as error:
            print(error)
        
