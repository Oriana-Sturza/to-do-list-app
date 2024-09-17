# To-Do List App

This project is a command-line-based To-Do List Manager that allows users to manage their tasks efficiently.

## Features

- **Add tasks**: Users can add new tasks to the list.
- **Complete tasks**: Mark tasks as completed.
- **Delete tasks**: Remove tasks from the list.
- **View tasks**: Display the list of tasks with their completion status (✔ for completed tasks, ✖ for incomplete tasks).

## How It Works

This To-Do List app stores tasks in a `tasks.json` file and allows users to perform various operations on tasks such as adding new tasks, marking them as complete, deleting them, and viewing the entire list.

## Technologies Used

- **Python**: The app is written in Python, making it easy to use and run on any platform that supports Python.
- **JSON**: Tasks are stored in a JSON file, which provides lightweight, structured data storage.

## Setup Instructions

To run this app on your machine, follow these steps:

### 1. Clone the Repository

You can download the project by cloning this repository to your local machine:

```bash
git clone https://github.com/your-github-username/to-do-list-app.git
```

2. Navigate to the Project Directory:
cd to-do-list-app

3. Run the App:
If Python is installed on your system, simply run the following command:
python to_do_list.py

4. Commands:
Inside the app, you can use the following commands to manage tasks:


add: Add a new task to the list.

complete: Mark an existing task as completed.

delete: Remove a task from the list.

quit: Exit the app.

Example Usage:

Enter command: add
Enter task title: Buy groceries
Task 'Buy groceries' added!

Enter command: complete
Enter task number to complete: 1
Task 'Buy groceries' marked as completed!

Enter command: delete
Enter task number to delete: 1
Task 'Buy groceries' deleted!

Enter command: quit

Future Improvements:

Task Prioritization: Add support for prioritizing tasks (e.g., high, medium, low).

Due Dates: Add an option to include deadlines for tasks.

Search Functionality: Implement a search feature to find tasks by name or status.

User Interface: Develop a graphical user interface (GUI) for more intuitive task management.


Contributing:

Feel free to contribute to this project by submitting issues or pull requests. If you'd like to work on a feature or bug, create a new branch and open a pull request for review.

