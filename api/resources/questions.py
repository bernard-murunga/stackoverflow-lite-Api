import datetime


now = datetime.datetime.now()

questions_dictionary = [
    {
        "user_id": 1,
        "question_id": 1,
        "question_title": "Linting",
        "question_details": "What does linting do?",
        "created_at": str(now),
        "updated_at": str(now)
    },
    {
        "user_id": 2,
        "question_id": 2,
        "question_title": "Testing",
        "question_details": "What is TDD?",
        "created_at": str(now),
        "updated_at": str(now)
    }
    ]