import requests

GET_ENDPOINT = 'http://127.0.0.1:8000'
POST_ENDPOINT = 'http://127.0.0.1:8000/add'

def test_call_endpoint():
    response = requests.get(GET_ENDPOINT)
    response_two = requests.get(POST_ENDPOINT)
    assert response.status_code == 200
    assert response_two.status_code == 200