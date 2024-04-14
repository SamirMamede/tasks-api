from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Tasks

class TasksViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Tasks.objects.create(task="Task 1")
        self.task2 = Tasks.objects.create(task="Task 2")

    def test_get_all_tasks(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
          
    def test_get_task_by_id(self):
        response = self.client.get('/tasks/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('tasks/999/')  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_task(self):
        data = {'task': 'New Task'}
        response = self.client.post('/tasks/add', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        data = {'task': 'Task Update'}
        response = self.client.put('/tasks/1/update', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put('/tasks/999/update', data)  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        response = self.client.delete(f'/tasks/{self.task1.pk}/delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/tasks/999/delete')  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
