## InovaTask API

This is a simple API for managing tasks. It allows you to create, list, update and delete tasks.

1. Clone this repository:

```bash
git clone https://github.com/SamirMamede/tasks-api.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```


3. Run Django migrations:

```
python manage.py migrate
```

4. Start the server:

```
python manage.py runserver
```

## Use

### Routes

- `GET ''`: List all tasks.
- `POST tasks/add/`: Create a new task.
- `GET tasks/{id}/`: Returns a specific task.
- `PUT tasks/{id}/update/`: Update an existing task.
- `DELETE tasks/{id}/delete/`: Deletes an existing task.

### Request example (POST /tasks/add/)

```json
{
  "task": "My new task"
}
```
### Response example (GET /tasks/1/)

```json
{
  "id": 1,
  "task": "My new task",
  "created": "2024-03-25T02:57:32.097680Z"
}
```