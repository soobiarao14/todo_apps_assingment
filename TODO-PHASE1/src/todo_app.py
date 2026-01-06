"""Main CLI application for Phase I Todo App.

This module provides the command-line interface for interacting with
the todo application. It displays a menu, handles user input, and
calls TaskManager methods to perform operations.
"""

import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from task_manager import TaskManager


def display_menu():
    """Display the main menu."""
    print("\n===== Todo App Menu =====")
    print("1. View all tasks")
    print("2. Add new task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Toggle task complete/incomplete")
    print("6. Exit")
    print("==========================")


def get_menu_choice():
    """Get and validate menu choice from user.

    Returns:
        int: Valid menu choice (1-6), or None if invalid
    """
    try:
        choice = int(input("Enter your choice (1-6): "))
        if 1 <= choice <= 6:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return None


def get_task_id():
    """Get and validate task ID from user.

    Returns:
        int: Task ID, or None if invalid
    """
    try:
        task_id = int(input("Enter task ID: "))
        return task_id
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")
        return None


def handle_view_tasks(manager):
    """Handle viewing all tasks.

    Args:
        manager: TaskManager instance
    """
    print("\n--- All Tasks ---")
    success, message = manager.view_tasks()
    print(message)


def handle_add_task(manager):
    """Handle adding a new task.

    Args:
        manager: TaskManager instance
    """
    print("\n--- Add New Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description (optional, press Enter to skip): ")

    success, message = manager.add_task(title, description)
    print(message)


def handle_update_task(manager):
    """Handle updating an existing task.

    Args:
        manager: TaskManager instance
    """
    print("\n--- Update Task ---")
    task_id = get_task_id()

    if task_id is None:
        return

    new_title = input("Enter new title: ")
    new_description = input("Enter new description (optional, press Enter to skip): ")

    success, message = manager.update_task(task_id, new_title, new_description)
    print(message)


def handle_delete_task(manager):
    """Handle deleting a task.

    Args:
        manager: TaskManager instance
    """
    print("\n--- Delete Task ---")
    task_id = get_task_id()

    if task_id is None:
        return

    success, message = manager.delete_task(task_id)
    print(message)


def handle_toggle_complete(manager):
    """Handle toggling task completion status.

    Args:
        manager: TaskManager instance
    """
    print("\n--- Toggle Task Complete/Incomplete ---")
    task_id = get_task_id()

    if task_id is None:
        return

    success, message = manager.toggle_complete(task_id)
    print(message)


def main():
    """Main application loop."""
    print("\n" + "="*50)
    print("Welcome to Todo CLI - Phase I")
    print("In-memory task management (data lost on exit)")
    print("="*50)

    manager = TaskManager()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice is None:
            continue

        if choice == 1:
            handle_view_tasks(manager)
        elif choice == 2:
            handle_add_task(manager)
        elif choice == 3:
            handle_update_task(manager)
        elif choice == 4:
            handle_delete_task(manager)
        elif choice == 5:
            handle_toggle_complete(manager)
        elif choice == 6:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
