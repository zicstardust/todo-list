from django.test import TestCase
from .models import Todo
from django.utils import timezone


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title="test", details="test")
        Todo.objects.create(title="test2", details="test2")

    def test_todo(self):
        test = Todo.objects.get(title="test")
        test2 = Todo.objects.get(title="test2")

        self.assertEqual(test.title, 'test')
        self.assertEqual(test.details, 'test')

        self.assertEqual(test2.title, 'test2')
        self.assertEqual(test2.details, 'test2')
