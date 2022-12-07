from django.test import TestCase
from django.urls import reverse

class TodoViewTest(TestCase):
    def test_single_task_non_important(self):
        response = self.client.get(
            reverse("todo_list:todo"),
            # {"todo": "task", "important": "false"}
        )
        self.assertEqual(response.status_code, 200)
