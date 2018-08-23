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



