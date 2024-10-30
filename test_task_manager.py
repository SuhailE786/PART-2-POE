import unittest
from task_manager import Task

class TestTaskManager(unittest.TestCase):
    def test_task_id_generation(self):
        # Test if Task ID is generated correctly
        task = Task("Login", "Create login feature", "John Doe", 8, "To Do")
        expected_task_id_prefix = "LO:"  # Task ID should start with the first two letters of task name
        self.assertTrue(task.task_id.startswith(expected_task_id_prefix))
        self.assertTrue(task.task_id.endswith("DOE"))  # Task ID should end with the last 3 letters of developer name

    def test_task_description_length_valid(self):
        # Test if task description meets length requirement
        task = Task("Login", "Short description", "John Doe", 8, "To Do")
        self.assertTrue(len(task.description) <= 50)

    def test_task_description_length_invalid(self):
        # Test if task description exceeds length requirement
        task_description = "This description is definitely more than fifty characters long and should fail"
        with self.assertRaises(ValueError):
            Task("Login", task_description, "John Doe", 8, "To Do")

    def test_task_creation(self):
        # Test if Task object is created successfully with correct details
        task = Task("Add Feature", "Add new feature to the project", "Jane Smith", 10, "Doing")
        self.assertEqual(task.name, "Add Feature")
        self.assertEqual(task.developer, "Jane Smith")
        self.assertEqual(task.duration, 10)
        self.assertEqual(task.status, "Doing")

    def test_display_task_details(self):
        # Test if task details are displayed correctly
        task = Task("Login", "Create login feature", "John Doe", 8, "To Do")
        details = task.display_task_details()
        self.assertIn("Task Status: To Do", details)
        self.assertIn("Developer: John Doe", details)
        self.assertIn("Task Name: Login", details)

    def test_total_hours(self):
        # Test if the total duration of all tasks is correctly accumulated
        task1 = Task("Task1", "Description", "John Doe", 5, "To Do")
        task2 = Task("Task2", "Another description", "Jane Doe", 8, "Doing")
        tasks = [task1, task2]
        total_hours = sum(task.get_task_duration() for task in tasks)
        self.assertEqual(total_hours, 13)

    def test_task_status_selection(self):
        # Test if status selection is handled correctly
        task = Task("Update", "Update feature", "Alice Brown", 4, "Done")
        self.assertEqual(task.status, "Done")

if __name__ == "__main__":
    unittest.main()
