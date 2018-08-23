import psycopg2
from api.db_connect import conn, cur

def question_exists(question_list, question_title, question_details):
    """ Check that question with same title and details already exists """
    for question in question_list:
        if question['question_title'] == question_title:
            return 'Question title is a duplicate'
        # if question['question_details'] == question_details:
        #     return 'Question details is a duplicate'


