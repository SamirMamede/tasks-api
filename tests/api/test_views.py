from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Tasks

class TasksViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Tasks.objects.create(task="Tarefa 1")
        self.task2 = Tasks.objects.create(task="Tarefa 2")

    def test_get_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  
    def test_get_task(self):
        response = self.client.get(f'/api/task/{self.task1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/task/999/')  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_tasks(self):
        data = {'task': 'Nova Tarefa'}
        response = self.client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        data = {'task': 'Tarefa Atualizada'}
        response = self.client.put(f'/api/task/{self.task1.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.put('/api/task/999/', data)  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        response = self.client.delete(f'/api/task/{self.task1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete('/api/task/999/')  
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
