import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, name, description, developer, duration, status):
        if not self.checkTaskDescription(description):
            raise ValueError("Task description must be 50 characters or less.")
        
        self.name = name
        self.description = description
        self.developer = developer
        self.duration = duration
        self.status = status
        self.task_id = self.createTaskID()

    def checkTaskDescription(self, description):
        """Checks if the task description is within the allowed length."""
        return len(description) <= 50

    def createTaskID(self):
        """Creates and returns the task ID."""
        # Generate Task ID: first two letters of name, length of name, last three letters of developer's name
        return f"{self.name[:2].upper()}:{len(self.name)}:{self.developer[-3:].upper()}"

    def printTaskDetails(self):
        """Returns the full task details."""
        return (f"Task Status: {self.status}\n"
                f"Developer: {self.developer}\n"
                f"Task Number: {len(self.name)}\n"
                f"Task Name: {self.name}\n"
                f"Task Description: {self.description}\n"
                f"Task ID: {self.task_id}\n"
                f"Duration: {self.duration} hrs")

    def show_task_details_popup(self):
        """Displays task details in a Tkinter popup."""
        details = self.printTaskDetails()
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showinfo("Task Details", details)

    def returnTotalHours(self):
        """Returns the duration of the task."""
        return self.duration

def task_management():
    print("Welcome to EasyKanban")
    tasks = []

    while True:
        print("\nPlease choose an option:")
        print("1. Add Tasks")
        print("2. Display All Tasks")
        print("3. Search for a Task")
        print("4. Generate Task Report")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Ask the user how many tasks they want to add
            try:
                num_tasks = int(input("How many tasks would you like to add? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            for i in range(num_tasks):
                print(f"\nAdding Task {i + 1} of {num_tasks}:")
                
                name = input("Enter task name: ")
                description = input("Enter task description (<= 50 characters): ")
                while len(description) > 50:
                    print("Please enter a task description of less than 50 characters")
                    description = input("Enter task description: ")

                developer = input("Enter developer name: ")
                duration = input("Enter task duration in hours: ")
                while not duration.isdigit():
                    print("Invalid input. Duration must be a number.")
                    duration = input("Enter task duration in hours: ")
                duration = int(duration)

                status = input("Enter task status (To Do / Done / Doing): ")
                while status not in ["To Do", "Done", "Doing"]:
                    print("Invalid status. Please enter one of the following: To Do, Done, Doing.")
                    status = input("Enter task status (To Do / Done / Doing): ")

                try:
                    task = Task(name, description, developer, duration, status)
                    tasks.append(task)
                    print("Task successfully captured.")
                    # Show the task details in a pop-up window
                    task.show_task_details_popup()
                except ValueError as e:
                    print(e)

        elif choice == "2":
            # Displaying all tasks after adding them
            if tasks:
                print("\nTask Report:")
                for task in tasks:
                    print(task.printTaskDetails())
                    print("-----------------------------")
                
                # Calculate and display the total hours for all tasks
                total_hours = sum(task.returnTotalHours() for task in tasks)
                print(f"\nTotal hours for all tasks: {total_hours} hrs")
            else:
                print("No tasks available to display.")

        elif choice == "3":
            # Search for a task by name or developer
            search_query = input("Enter the task name or developer name to search for: ").lower()
            found_tasks = [task for task in tasks if search_query in task.name.lower() or search_query in task.developer.lower()]
            
            if found_tasks:
                print(f"\nFound {len(found_tasks)} matching task(s):")
                for task in found_tasks:
                    print(task.printTaskDetails())
                    print("-----------------------------")
            else:
                print("No tasks found matching your search criteria.")

        elif choice == "4":
            # Generate task report
            print("\nPlease choose the type of report:")
            print("1. View All Tasks Grouped by Status")
            print("2. View All Tasks Assigned to a Developer")
            report_choice = input("Enter your choice: ")

            if report_choice == "1":
                # Group tasks by status
                statuses = {"To Do": [], "Doing": [], "Done": []}
                for task in tasks:
                    statuses[task.status].append(task)

                for status, task_list in statuses.items():
                    print(f"\nTasks with status '{status}':")
                    if task_list:
                        for task in task_list:
                            print(task.printTaskDetails())
                            print("-----------------------------")
                    else:
                        print("No tasks with this status.")

            elif report_choice == "2":
                # View tasks assigned to a specific developer
                developer_name = input("Enter the developer name: ").lower()
                developer_tasks = [task for task in tasks if task.developer.lower() == developer_name]

                if developer_tasks:
                    print(f"\nTasks assigned to {developer_name}:")
                    for task in developer_tasks:
                        print(task.printTaskDetails())
                        print("-----------------------------")
                else:
                    print(f"No tasks found for developer: {developer_name}")

            else:
                print("Invalid report choice. Please try again.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    task_management()
