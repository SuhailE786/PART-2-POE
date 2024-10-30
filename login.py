import re

class Login:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def check_username(self, username):
        """Ensures username contains an underscore and is <= 5 characters."""
        if "_" in username and len(username) <= 5:
            return True
        return False

    def check_password_complexity(self, password):
        """Ensures that the password is at least 8 characters long, contains a capital letter, a number, and a special character."""
        if (len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"\d", password) and
            re.search(r"[^a-zA-Z0-9]", password)):
            return True
        return False

    def register_user(self, username, password, first_name, last_name):
        """Registers the user if both the username and password are valid."""
        if not self.check_username(username):
            return "Username is not correctly formatted, please ensure that your username contains an underscore and is no more than 5 characters in length."
        if not self.check_password_complexity(password):
            return "Password is not correctly formatted, please ensure that the password contains at least 8 characters, a capital letter, a number, and a special character."
        
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        return "User registered successfully!"

    def login_user(self, username, password):
        """Verifies if the login details are correct."""
        if username == self.username and password == self.password:
            return True
        return False

    def return_login_status(self, username, password):
        """Returns login status based on the entered username and password."""
        if self.login_user(username, password):
            return f"Welcome {self.first_name} {self.last_name}, it is great to see you again."
        else:
            return "Username or password incorrect, please try again."

def main():
    login_system = Login()
    is_logged_in = False  # This flag keeps track of whether the user is logged in

    while True:
        print("\nWelcome to the system. Please choose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Task Management (Requires Login)")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            print(login_system.register_user(username, password, first_name, last_name))

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login_system.login_user(username, password):
                is_logged_in = True
                print(login_system.return_login_status(username, password))
                print("\nWelcome to EasyKanban!")  # Welcome message after successful login
            else:
                print("Login failed. Please try again.")

        elif choice == "3":
            if is_logged_in:
                # Importing task_management from task_manager
                from task_manager import task_management
                print("\nWelcome to EasyKanban Task Management!")  # Welcome message before task management
                task_management()
            else:
                print("You need to be logged in to manage tasks. Please log in first.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()