from django.test import RequestFactory, TestCase
from api.views import getTasks

class TestGetTasksView(TestCase):
    def test_get_tasks_success(self):
        factory = RequestFactory()

        request = factory.get('')
        response = getTasks(request)
        self.assertEqual(response.status_code, 200)