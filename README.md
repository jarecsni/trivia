# Full Stack API Final Project


## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter) and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom.
>Once you're ready, you can submit your project on the last page.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend
The [./backend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


### Frontend

The [./frontend](https://github.com/udacity/FSND/blob/master/projects/02_trivia_api/starter/frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. If you have prior experience building a frontend application, you should feel free to edit the endpoints as you see fit for the backend you design. If you do not have prior experience building a frontend application, you should read through the frontend code before starting and make notes regarding:

1. What are the end points and HTTP methods the frontend is expecting to consume?
2. How are the requests from the frontend formatted? Are they expecting certain parameters or payloads? 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. The places where you may change the frontend behavior, and where you should be looking for the above information, are marked with `TODO`. These are the files you'd want to edit in the frontend:

1. *./frontend/src/components/QuestionView.js*
2. *./frontend/src/components/FormView.js*
3. *./frontend/src/components/QuizView.js*


By making notes ahead of time, you will practice the core skill of being able to read and understand code and will have a simple plan to follow to build out the endpoints of your backend API. 



>View the [README within ./frontend for more details.](./frontend/README.md)


## API Reference

### 1. Endpoint documentation

### [GET /categories]
Return a list of all categories in the application.

#### Request 
**Method**: GET
**Query Params**: NONE

#### Response
**Type**: JSON

**Attributes**:

    - categories: object with category ids as keys, and category names as values.
    - success: True for a successful request

#### Example

**Request**
```curl http://localhost:5000/categories```

**Response**
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

### [DELETE /questions/<id>[?page=<int:page>]]
Delete the question with the specified ID if one exists. 

#### Request 
**Method**: DELETE
**Query Params**: 
    - id: id of the question to be deleted
    - page: number of page to return questions for (optional)

#### Response
**Type**: JSON

**Attributes**:

    - categories: object with category ids as keys, and category names as values.
    - success: True for a successful request

#### Example

**Request**
```curl -X DELETE http://localhost:5000/questions/12?page=2 ```

**Response**
```
{
  "success": true,
  "deleted": 12,
  "questions": [...],
  "total_questions": 29
}
```

### [POST /questions]
Create new question with the values submitted for 'question', 'answer', 'difficulty' and 'category'. 

#### Request 
**Method**: POST
**Query Params**: None
**Payload**: 

    - "question": the new question 
    - "answer": the answer for the new question
    - "difficulty": value between 1 and 5 denoting difficulty
    - "category": an existing category id


#### Response
**Type**: JSON

**Attributes**:

    - created: id of the newly created question
    - success: True for a successful request
    - questions: current questions (array of question objects)
    - total_questions: number of questions in the database

#### Example

**Request**
```curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Who created the iPhone?", "answer": "Steve Jobs","category" :"1", "difficulty":"2"}'```

**Response**
```
{
  "created": 92, 
  "questions": [<list of current questions>],
  "success": True, 
  "total_questions": 102
}
```

### [POST /questions]
Search for questions using the submitted searchTerm.

NOTE: Based on the payload the questions endpoint with POST has two different behaviour. If a searchTerm attribute is present in the payload, it will return a list of questions matching the searchTerm, otherwise it will create a new question. 

#### Request 
**Method**: POST
**Query Params**: None
**Payload**: 

    - "searchTerm": search term; any questions with partial match will be returned
   

#### Response
**Type**: JSON

**Attributes**:

    - categories: object with category ids as keys, and category names as values.
    - success: True for a successful request

#### Example

**Request**
```curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"first"}'```

**Response**
```
{
    "questions":[
        { 
            "answer":"Tom Cruise",
            "category":5,
            "difficulty":4,
            "id":4,
            "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer":"Uruguay",
            "category":6,
            "difficulty":4,
            "id":11,
            "question":"Which country won the first ever soccer World Cup in 1930?"
        }
    ],
    "success":true,
    "total_questions":2
}
```

### [GET /categories/<int:id>/questions?page=<int:page>]
Returns a pageful of the questions belonging to the specified category

#### Request 
**Method**: GET
**Query Params**:
    - id: the category id
    - page: pagination index

#### Response
**Type**: JSON

**Attributes**:

    - questions: a pageful of question objects in the current category
    - success: True for a successful request
    - total_questions: number of questions in the specified category

#### Example

**Request**
```curl http://localhost:5000/categories/3/questions```

**Response**
{
  "current_category": "Geography", 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": "3", 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

### [POST /quizzes]
Return a random question in the category, excluding any previously returned questions (as specified in request payload, see below)

#### Request 
**Method**: POST
**Query Params**: None
**Payload**: 

    - "category": the category to filter questions for
    - "previous_questions": array of question ids which have already been played
   

#### Response
**Type**: JSON

**Attributes**:

    - "question": random question from category that has not been asked (can be None!)
    - "success": True for a successful request

#### Example

**Request**
```
curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"quiz_category":{type: "Art", id: "2"}, "previous_questions":[18]}'
```

**Response**
```
{
    "questions":[
        { 
            "question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4
        },
        {
            "question": "Which country won the first ever soccer World Cup in 1930?",
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11
        }
    ],
    "success":true,
    "total_questions":2
}
```


## 2. Error Handling
When an error occurs the endpoint sets the correct HTTP status code in the response as

400: Bad Request
404: Resource Not Found
422: Not Processable
500: Internal Server Error

Details of the error are also available:

```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

