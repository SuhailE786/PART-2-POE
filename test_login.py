import unittest
from login import Login

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = Login()

    def test_check_username_valid(self):
        self.assertTrue(self.login.check_username("user_"))

    def test_check_username_invalid(self):
        self.assertFalse(self.login.check_username("username"))

    def test_check_password_complexity_valid(self):
        self.assertTrue(self.login.check_password_complexity("Password1@"))

    def test_check_password_complexity_invalid(self):
        self.assertFalse(self.login.check_password_complexity("password"))

    def test_register_user_success(self):
        response = self.login.register_user("user_", "Password1@", "John", "Doe")
        self.assertEqual(response, "User registered successfully!")

    def test_register_user_invalid_username(self):
        response = self.login.register_user("username", "Password1@", "John", "Doe")
        self.assertEqual(response, "Username is not correctly formatted, please ensure that your username contains an underscore and is no more than 5 characters in length.")

    def test_register_user_invalid_password(self):
        response = self.login.register_user("user_", "password", "John", "Doe")
        self.assertEqual(response, "Password is not correctly formatted, please ensure that the password contains at least 8 characters, a capital letter, a number, and a special character.")

    def test_login_user_successful(self):
        self.login.register_user("user_", "Password1@", "John", "Doe")
        self.assertTrue(self.login.login_user("user_", "Password1@"))

    def test_login_user_unsuccessful(self):
        self.login.register_user("user_", "Password1@", "John", "Doe")
        self.assertFalse(self.login.login_user("user_", "wrongPassword"))

    def test_return_login_status_successful(self):
        self.login.register_user("user_", "Password1@", "John", "Doe")
        response = self.login.return_login_status("user_", "Password1@")
        self.assertEqual(response, "Welcome John Doe, it is great to see you again.")

    def test_return_login_status_unsuccessful(self):
        self.login.register_user("user_", "Password1@", "John", "Doe")
        response = self.login.return_login_status("user_", "wrongPassword")
        self.assertEqual(response, "Username or password incorrect, please try again.")

if __name__ == "__main__":
    unittest.main()
