import requests

GET_ENDPOINT = 'http://127.0.0.1:8000'
POST_ENDPOINT = 'http://127.0.0.1:8000/add'

def test_get_tasks_success():
    response = requests.get(GET_ENDPOINT)
    assert response.status_code == 200

def test_get_tasks_empty():
    response = requests.get(GET_ENDPOINT)
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_get_tasks_response_format():
    response = requests.get(GET_ENDPOINT)
    assert response.status_code == 200
    data = response.json()
    for task in data:
        assert 'id' in task
        assert 'task' in task
        assert 'created' in task