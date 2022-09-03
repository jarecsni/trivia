from multiprocessing import connection
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format('trivia', 'trivia', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            #self.db.create_all()
            with self.db.engine.connect() as connection:
                file = open("./trivia_load.psql")
                stmts = text(file.read())
                connection.execute(stmts)

    
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            with self.db.engine.connect() as connection:
                file = open("./trivia_del.psql")
                stmts = text(file.read())
                connection.execute(stmts)
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # -------------------------------
    # /questions (GET)
    # -------------------------------
    def test_paginated_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 19)
        self.assertEqual(len(data["questions"]), 10)

    def test_paginated_questions_when_page_exists(self):
        res = self.client().get("/questions?page=2")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 19)
        self.assertEqual(len(data["questions"]), 9)

    def test_paginated_questions_when_page_does_not_exists(self):
        res = self.client().get("/questions?page=2000")
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    # -------------------------------
    # /categories (GET)
    # -------------------------------
    def test_categories_return_values(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data["categories"]), 6)

    def test_when_there_are_no_categories(self):
        self.tearDown()
        res = self.client().get("/categories")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        
    # -------------------------------
    # /questions/<id> (DELETE)
    # -------------------------------
    def test_delete_question(self):
        res = self.client().delete("/questions/5")
        self.assertEqual(res.status_code, 200);
        res = self.client().delete("/questions/5")
        self.assertEqual(res.status_code, 404);

    # -------------------------------
    # /questions (POST)
    # -------------------------------
    def test_post_new_question(self):
        res = self.client().post("/questions", json={
            'question': 'Some question', 
            'answer': 'Some answer',
            'difficulty': 4,
            'category': 1
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['total_questions'], 20)
        self.assertEqual(data['created'], 1)

    def test_post_search_question(self):
        res = self.client().post("/questions", json={
            'searchTerm': 'What'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['questions']), 8)

    def test_post_search_question_with_no_match(self):
        res = self.client().post("/questions", json={
            'searchTerm': 'DefinitelyNoSuchQuestionLikeThisSearchTerm'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data['questions']), 0)
        

    # -------------------------------
    # /categories/<category>/questions (GET)
    # -------------------------------
    def test_get_questions_of_a_category(self):
        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data["questions"]), 3)

    def test_get_questions_of_a_category_with_nonexistent_category(self): 
        res = self.client().get("/categories/100/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(data["questions"]), 0)

    # -------------------------------
    # /quizzes (POST)
    # -------------------------------
    def test_error_is_returned_for_empty_request_body(self):
        res = self.client().post("/quizzes")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_quiz_question_returned_with_no_previous_question(self):
        res = self.client().post("/quizzes", json={
            'quiz_category': {'type':'Science', 'id': '1'},
            'previous_questions': []
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['question'])
        self.assertTrue(data['success'])



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()