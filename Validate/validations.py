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



