import psycopg2
from api.db_connect import conn, cur

def question_exists(question_list, question_title, question_details):
    """ Check for duplicate question titles """
    for question in question_list:
        if question['question_title'] == question_title:
            return 'Question title is a duplicate'
        # if question['question_details'] == question_details:
        #     return 'Question details is a duplicate'


def question_id_found(question_list, question_id):
    """check for single question existence"""

    for question in question_list:
        if question['question_title'] == question_id:
            return 'Question exists'


def duplicate_answer(answer_details):
    # checking if answer already exists
            
    try:
        cur.execute("SELECT * FROM answers")
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
        
    results = cur.fetchall()    

    for result in results:
        if result[3] == answer_details:
            return 'Answer exists'


def check_question_author(user_id, question_id):
        #  check question author so that they can accept answers

        query = "SELECT * FROM questions WHERE question_id = %s;"
        cur.execute(query, [question_id])
        result = cur.fetchall()

        for i in result:
            if i[1] != user_id:  ## user_id is at index 1 in answers table
                return "You don't have permission to accept answer"


def check_user_duplication(all_users, username, email):
    #check if user exists already

    for user in all_users:
        if user[1] == username:
            return 'Username is taken, try another'
        if user[2] == email:
            return 'Email already in use, try another'


def validate_username(username):
    #  validate user input fields

    if not isinstance(username,str):
        return 'Please use words in username'

