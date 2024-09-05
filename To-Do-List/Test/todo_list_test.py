import unittest
from datetime import datetime
from todo_list import Task  

class TestTask(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.task = Task()

    def test_task_name(self):
        self.assertIsInstance(self.task.task_name, str)

    def test_task_category(self):
        valid_categories = ['Personal', 'Work', 'Education', 'Other']
        self.assertIn(self.task.task_category, valid_categories)

    def test_task_priority(self):
        valid_priorities = ['High', 'Medium', 'Low']
        self.assertIn(self.task.priority, valid_priorities)

    def test_task_status(self):
        valid_statuses = ['Not Started', 'In Progress', 'Completed', 'Uncompleted']
        self.assertIn(self.task.task_status, valid_statuses)

    def test_creation_date(self):
        try:
            datetime.strptime(self.task.creation_date, '%Y-%m-%d')
        except ValueError:
            self.fail("Creation date is not in the correct format")

    def test_end_date(self):
        if self.task.task_status == 'Completed':
            self.assertEqual(self.task.end_date, datetime.now().strftime('%Y-%m-%d'))
        else:
            try:
                datetime.strptime(self.task.end_date, '%Y-%m-%d')
            except ValueError:
                self.fail("End date is not in the correct format")

    def test_task_description(self):
        self.assertIsInstance(self.task.task_description, str)

if __name__ == '__main__':
    unittest.main()
