import datetime


now = datetime.datetime.now()

answers_dictionary = [
    {
        "user_id": 1,
        "question_id": 1,
        "answer_id": 1,
        "answer_details": "Highlight syntax",
        "preferred": "no",
        "create_at": str(now),
        "updated_at": str(now)
    },
    {
        "user_id": 2,
        "question_id": 2,
        "answer_id": 2,
        "answer_details": "Testing code to ensure it has no errors.",
        "preferred": "no",
        "create_at": str(now),
        "updated_at": str(now)
    }
    ]