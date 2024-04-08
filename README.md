## InovaTask API

This is a simple API for managing tasks. It allows you to create, list, update and delete tasks.

1. Install dependencies:

'''
pip install -r requirements.txt
'''


2. Run Django migrations:

'''
python manage.py migrate
'''

3. Start the server:

'''
python manage.py runserver
'''

## Use

### Routes

- `GET ''`: List all tasks.
- `POST tasks/add/`: Create a new task.
- `GET tasks/{id}/`: Returns a specific task.
- `PUT tasks/{id}/update/`: Update an existing task.
- `DELETE tasks/{id}/delete/`: Deletes an existing task.

### Request example (POST /tasks/)

```json
{
  "task": "My new task"
}