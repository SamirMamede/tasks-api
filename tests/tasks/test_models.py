from django.test import TestCase
from datetime import datetime
from tasks.models import Tasks

class TasksModelTestCase(TestCase):
    def setUp(self):
        self.task = Tasks.objects.create(task="Task test")

    def test_create_task(self):
        self.assertEqual(self.task.task, "Task test")
        self.assertIsInstance(self.task.created, datetime)

    def test_validate_field_task(self):
        with self.assertRaises(Exception):
            Tasks.objects.create()

    def test_date_created(self):
        now = datetime.now()
        self.assertLess(self.task.created, now)

    def test_update_task(self):
        self.task.task = "Update task"
        self.task.save()
        self.assertEqual(self.task.task, "Update task")

    def test_delete_task(self):
        self.task.delete()
        self.assertFalse(Tasks.objects.filter(task="Task test").exists())
