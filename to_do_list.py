import json

# File where tasks will be saved
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Loads tasks from the JSON file.
    Returns a list of tasks or an empty list if no tasks are found.
    """
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)  # Load tasks from the file
    except FileNotFoundError:
        return []  # If the file is not found, return an empty list

def save_tasks(tasks):
    """
    Saves tasks to the JSON file.
    Args:
        tasks (list): List of tasks to be saved.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)  # Write tasks to the file

def display_tasks(tasks):
    """
    Displays all tasks in the list.
    Args:
        tasks (list): List of tasks to be displayed.
    """
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks added yet.")
    for idx, task in enumerate(tasks):
        status = "✔" if task['completed'] else "✖"
        print(f"{idx + 1}. {task['title']} [{status}]")

def add_task(tasks, title):
    """
    Adds a new task to the list.
    Args:
        tasks (list): The current list of tasks.
        title (str): The title of the task to be added.
    """
    tasks.append({"title": title, "completed": False})  # Append the new task to the list
    save_tasks(tasks)  # Save the updated list of tasks
    print(f"Task '{title}' added!")

def mark_task_complete(tasks, index):
    """
    Marks a task as completed.
    Args:
        tasks (list): The current list of tasks.
        index (int): The index of the task to mark as completed.
    """
    if 0 <= index < len(tasks):  # Ensure the task index is valid
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index]['title']}' marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(tasks, index):
    """
    Deletes a task from the list.
    Args:
        tasks (list): The current list of tasks.
        index (int): The index of the task to delete.
    """
    if 0 <= index < len(tasks):  # Ensure the task index is valid
        removed_task = tasks.pop(index)  # Remove the task from the list
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted!")
    else:
        print("Invalid task number.")

def main():
    """
    Main function to run the to-do list manager.
    Handles user input and actions.
    """
    tasks = load_tasks()  # Load existing tasks from the file
    while True:
        display_tasks(tasks)
        print("\nCommands: add, complete, delete, quit")
        command = input("Enter command: ").lower()

        if command == "add":
            title = input("Enter task title: ")
            add_task(tasks, title)
        elif command == "complete":
            try:
                index = int(input("Enter task number to complete: ")) - 1
                mark_task_complete(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "delete":
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(tasks, index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "quit":
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
