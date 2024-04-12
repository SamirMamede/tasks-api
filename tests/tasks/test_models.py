from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.timezone import make_aware
from datetime import datetime
from tasks.models import Tasks

class TasksModelTestCase(TestCase):
    def setUp(self):
        self.task = Tasks.objects.create(task="Task test")

    def test_create_task(self):
        self.assertEqual(self.task.task, "Task test")
        self.assertIsInstance(self.task.created, datetime)

    def test_validate_field_task(self):
        with self.assertRaises(ValidationError):
            Tasks.objects.create(task="New task")

    def test_date_created(self):
        now = datetime.now()
        now_aware = make_aware(now)
        self.assertLess(self.task.created, now_aware)

    def test_update_task(self):
        self.task.task = "Update task"
        self.task.save()
        self.assertEqual(self.task.task, "Update task")

    def test_delete_task(self):
        self.task.delete()
        self.assertFalse(Tasks.objects.filter(task="Task test").exists())
