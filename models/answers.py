import psycopg2
from api.db_connect import conn, cur

class Answers_model():    
    # def __init__(self, question_id, answer_details, user_id):
    #     self.question_id = question_id
    #     self.answer_details = answer_details
    #     self.user_id = user_id


    def post_answer(user_id, question_id, answer_details):
        #  post answer to question

        data = dict(user_id = user_id, question_id = question_id,
                    answer_details = answer_details)
        
        try:

            cur.execute("""INSERT INTO answers(user_id, question_id, answer_details, preferred , created_at) VALUES 
                    (%(user_id)s, %(question_id)s, %(answer_details)s, False, current_timestamp )""", data)

            conn.commit()

            return "Successfully added answer"

        except psycopg2.DatabaseError as error:
            print(error)


    def accept_answer(question_id, answer_id):
        #  mark answers as preferred
        try:
            query = "UPDATE answers SET preferred = true WHERE id = %s AND question_id = %s;"
            cur.execute(query, [answer_id, question_id])
            conn.commit()

            return "Successfully accepted answer"

        except psycopg2.DatabaseError as error:
            print(error)