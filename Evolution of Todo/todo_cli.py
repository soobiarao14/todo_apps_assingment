#!/usr/bin/env python3
"""
Phase I: CLI Todo Application
Evolution of Todo Project

A minimalist in-memory Python console application for todo task management.
Provides five basic operations (Add, View, Update, Delete, Mark Complete/Incomplete)
through a menu-driven CLI interface.

All data is stored in memory and lost on application exit.
No persistence, no external dependencies, no databases.

Author: Evolution of Todo Project
Version: Phase I
Python: 3.13+
"""

# ============ DATA LAYER ============

# ANSI Color Codes for CLI UI
COLOR_RESET = "\033[0m"
COLOR_HEADER = "\033[95m"    # Magenta
COLOR_SUCCESS = "\033[92m"   # Green
COLOR_ERROR = "\033[91m"     # Red
COLOR_INFO = "\033[94m"      # Blue
COLOR_BOLD = "\033[1m"

# Global in-memory storage
tasks = []        # List of task dictionaries
next_id = 1       # Auto-incrementing ID counter


def generate_id():
    """
    Generate and return the next unique task ID.

    Returns:
        int: The next available task ID (auto-incremented)

    Side Effects:
        Increments global next_id counter

    Guarantees:
        - Returned ID is unique and has never been used before
        - ID is always greater than all previously generated IDs
    """
    global next_id
    current_id = next_id
    next_id += 1
    return current_id


def find_task_by_id(task_id):
    """
    Find and return task by ID, or None if not found.

    Args:
        task_id (int): The ID of the task to find

    Returns:
        dict | None: Task dictionary if found, None otherwise

    Side Effects:
        None (read-only operation)

    Guarantees:
        - Returns reference to actual task (not a copy)
        - O(n) time complexity (acceptable for Phase I)
    """
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


# ============ BUSINESS LOGIC LAYER ============

def create_task(title, description=""):
    """
    Create a new task and add it to the task list.

    Args:
        title (str): Task title (required, non-empty)
        description (str): Optional task description (default: empty string)

    Returns:
        dict: The newly created task with all fields populated

    Raises:
        ValueError: If title validation fails

    Side Effects:
        - Appends new task to global tasks list
        - Increments global next_id counter

    Guarantees:
        - Task is added to tasks list
        - Task has unique auto-generated ID
        - Task completed field defaults to False
    """
    if not validate_title(title):
        raise ValueError("Title cannot be empty or whitespace")

    task = {
        "id": generate_id(),
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    return task


def get_all_tasks():
    """
    Return all tasks in insertion order (ascending ID).

    Returns:
        list[dict]: All tasks in ascending ID order

    Side Effects:
        None (read-only operation)

    Guarantees:
        - Returns reference to actual tasks list
        - Tasks are in insertion order (which equals ascending ID order)
        - Empty list returned if no tasks exist
    """
    return tasks


def update_task_fields(task, title=None, description=None):
    """
    Update task fields. At least one field must be provided.

    Args:
        task (dict): The task dictionary to update
        title (str | None): New title (if provided), or None to leave unchanged
        description (str | None): New description (if provided), or None to leave unchanged

    Raises:
        ValueError: If both title and description are None
        ValueError: If title validation fails

    Side Effects:
        Modifies task dictionary in-place within tasks list

    Guarantees:
        - Only provided fields are updated
        - Task ID and completion status remain unchanged
        - Changes are immediately visible in tasks list
    """
    if title is None and description is None:
        raise ValueError("At least one field (title or description) must be provided")

    if title is not None:
        if not validate_title(title):
            raise ValueError("Title cannot be empty or whitespace")
        task["title"] = title

    if description is not None:
        task["description"] = description


def delete_task_by_id(task_id):
    """
    Delete task by ID. Returns True if deleted, False if not found.

    Args:
        task_id (int): The ID of the task to delete

    Returns:
        bool: True if task was found and deleted, False otherwise

    Side Effects:
        Removes task from global tasks list (if found)
        Does NOT decrement next_id counter (IDs never reused)

    Guarantees:
        - Task is removed from tasks list if it exists
        - next_id remains unchanged (IDs are never reused)
        - All other tasks remain unchanged
    """
    task = find_task_by_id(task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


def toggle_task_completion(task_id):
    """
    Toggle task completion status. Returns True if toggled, False if not found.

    Args:
        task_id (int): The ID of the task to toggle

    Returns:
        bool: True if task was found and toggled, False otherwise

    Side Effects:
        Flips the completed field of the task (True ↔ False)

    Guarantees:
        - If task is found, completed field changes: False → True or True → False
        - All other fields remain unchanged
    """
    task = find_task_by_id(task_id)
    if task is None:
        return False
    task["completed"] = not task["completed"]
    return True


# ============ VALIDATION LAYER ============

def validate_title(title):
    """
    Validate that title is not empty or whitespace-only.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if title is valid, False otherwise

    Side Effects:
        None (pure function)

    Guarantees:
        - Returns False if title is None, empty string, or whitespace-only
        - Returns True for any string with at least one non-whitespace character
    """
    return title is not None and title.strip() != ""


def validate_menu_choice(choice):
    """
    Validate menu choice is between 1 and 6.

    Args:
        choice (int | None): The menu choice to validate

    Returns:
        bool: True if choice is valid (1-6), False otherwise

    Side Effects:
        None (pure function)

    Guarantees:
        - Returns True only if choice is exactly 1, 2, 3, 4, 5, or 6
        - Returns False for None, values < 1, or values > 6
    """
    return choice is not None and 1 <= choice <= 6


def get_int_input(prompt):
    """
    Get integer input from user. Returns None if input is invalid.

    Args:
        prompt (str): The prompt message to display

    Returns:
        int | None: Valid integer entered by user, or None for invalid input

    Side Effects:
        - Reads from stdin (blocks until user input)
        - Prints error message to stdout if input is invalid

    Guarantees:
        - Returns None (not an exception) for invalid input
        - Prints user-friendly error message on parse failure
    """
    try:
        return int(input(prompt))
    except ValueError:
        print(f"{COLOR_ERROR}Error: Please enter a valid number{COLOR_RESET}")
        return None


# ============ UI LAYER ============

def display_menu():
    """
    Display the main menu.

    Side Effects:
        Prints menu to stdout

    Guarantees:
        Displays exactly 6 menu options numbered 1-6
    """
    print(f"\n{COLOR_HEADER}{COLOR_BOLD}===== Todo Application ====={COLOR_RESET}")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print(f"{COLOR_HEADER}============================{COLOR_RESET}")


def display_tasks():
    """
    Display all tasks or an empty message.

    Side Effects:
        - Reads from global tasks list
        - Prints to stdout

    Guarantees:
        - If tasks is empty, displays "No tasks available"
        - If tasks is non-empty, displays each task with ID, title, and completion status
        - Tasks are shown in ascending ID order
    """
    if len(tasks) == 0:
        print(f"\n{COLOR_INFO}No tasks available.{COLOR_RESET}")
        return

    print(f"\n{COLOR_HEADER}{COLOR_BOLD}===== Task List ====={COLOR_RESET}")
    for task in tasks:
        if task["completed"]:
            status = f"{COLOR_SUCCESS}Complete{COLOR_RESET}"
        else:
            status = f"{COLOR_ERROR}Incomplete{COLOR_RESET}"
        print(f"[{task['id']}] {task['title']} ({status})")
    print(f"{COLOR_HEADER}====================={COLOR_RESET}")


def add_task_ui():
    """
    Handle Add Task menu option.

    Workflow:
        1. Prompt user for title
        2. Validate title (non-empty, non-whitespace)
        3. Prompt user for description (optional)
        4. Call create_task(title, description)
        5. Print success message with task ID

    Error Handling:
        If title is invalid, print error and return to menu (no task created)
    """
    print(f"\n{COLOR_INFO}--- Add Task ---{COLOR_RESET}")
    title = input("Enter task title: ")

    if not validate_title(title):
        print(f"{COLOR_ERROR}Error: Title cannot be empty or whitespace{COLOR_RESET}")
        return

    description = input("Enter task description (optional): ")

    try:
        task = create_task(title, description)
        print(f"{COLOR_SUCCESS}[OK] Task created successfully (ID: {task['id']}){COLOR_RESET}")
    except ValueError as e:
        print(f"{COLOR_ERROR}Error: {e}{COLOR_RESET}")


def view_tasks_ui():
    """
    Handle View Tasks menu option.

    Workflow:
        1. Call display_tasks() to show all tasks
    """
    display_tasks()


def update_task_ui():
    """
    Handle Update Task menu option.

    Workflow:
        1. Check if task list is empty; if so, print error and return
        2. Prompt user for task ID
        3. Validate ID is a number
        4. Find task by ID; if not found, print error and return
        5. Prompt user for new title (or press Enter to skip)
        6. Prompt user for new description (or press Enter to skip)
        7. Validate at least one field was provided
        8. Validate new title if provided
        9. Call update_task_fields()
        10. Print success message

    Error Handling:
        - Empty task list → "Error: Task list is empty"
        - Invalid ID format → "Error: Please enter a valid number"
        - Task not found → "Error: Task with ID {id} not found"
        - No fields provided → "Error: No changes made (both fields skipped)"
        - Invalid title → "Error: Title cannot be empty or whitespace"
    """
    if len(tasks) == 0:
        print(f"{COLOR_ERROR}Error: Task list is empty{COLOR_RESET}")
        return

    print(f"\n{COLOR_INFO}--- Update Task ---{COLOR_RESET}")
    task_id = get_int_input("Enter task ID to update: ")
    if task_id is None:
        return

    task = find_task_by_id(task_id)
    if task is None:
        print(f"{COLOR_ERROR}Error: Task with ID {task_id} not found{COLOR_RESET}")
        return

    print("(Press Enter to skip a field)")
    new_title = input(f"Enter new title (current: '{task['title']}'): ")
    new_description = input(f"Enter new description (current: '{task['description']}'): ")

    # Convert empty strings to None for skipped fields
    new_title = new_title if new_title else None
    new_description = new_description if new_description else None

    try:
        update_task_fields(task, title=new_title, description=new_description)
        print(f"{COLOR_SUCCESS}[OK] Task {task_id} updated successfully{COLOR_RESET}")
    except ValueError as e:
        print(f"{COLOR_ERROR}Error: {e}{COLOR_RESET}")


def delete_task_ui():
    """
    Handle Delete Task menu option.

    Workflow:
        1. Check if task list is empty; if so, print error and return
        2. Prompt user for task ID
        3. Validate ID is a number
        4. Call delete_task_by_id()
        5. Print success or error message based on result

    Error Handling:
        - Empty task list → "Error: Task list is empty"
        - Invalid ID format → "Error: Please enter a valid number"
        - Task not found → "Error: Task with ID {id} not found"
    """
    if len(tasks) == 0:
        print(f"{COLOR_ERROR}Error: Task list is empty{COLOR_RESET}")
        return

    print(f"\n{COLOR_INFO}--- Delete Task ---{COLOR_RESET}")
    task_id = get_int_input("Enter task ID to delete: ")
    if task_id is None:
        return

    if delete_task_by_id(task_id):
        print(f"{COLOR_SUCCESS}[OK] Task {task_id} deleted successfully{COLOR_RESET}")
    else:
        print(f"{COLOR_ERROR}Error: Task with ID {task_id} not found{COLOR_RESET}")


def toggle_completion_ui():
    """
    Handle Mark Complete/Incomplete menu option.

    Workflow:
        1. Check if task list is empty; if so, print error and return
        2. Prompt user for task ID
        3. Validate ID is a number
        4. Call toggle_task_completion()
        5. Print success or error message based on result

    Error Handling:
        - Empty task list → "Error: Task list is empty"
        - Invalid ID format → "Error: Please enter a valid number"
        - Task not found → "Error: Task with ID {id} not found"
    """
    if len(tasks) == 0:
        print(f"{COLOR_ERROR}Error: Task list is empty{COLOR_RESET}")
        return

    print(f"\n{COLOR_INFO}--- Mark Complete/Incomplete ---{COLOR_RESET}")
    task_id = get_int_input("Enter task ID to toggle: ")
    if task_id is None:
        return

    if toggle_task_completion(task_id):
        print(f"{COLOR_SUCCESS}[OK] Task {task_id} completion status toggled{COLOR_RESET}")
    else:
        print(f"{COLOR_ERROR}Error: Task with ID {task_id} not found{COLOR_RESET}")


# ============ MAIN ============

def main():
    """
    Main application loop.

    Workflow:
        - Display welcome message
        - Infinite loop:
            1. Display menu
            2. Get user choice
            3. Validate choice
            4. Dispatch to appropriate UI function
            5. Exit on choice 6

    Guarantees:
        - Application never crashes from invalid input (all errors handled)
        - User always returns to menu after each operation
        - Application only exits when user explicitly selects option 6
    """
    print("Welcome to the Todo CLI Application!")
    print("Note: All data is stored in memory and will be lost when you exit.")

    while True:
        display_menu()
        choice = get_int_input("Enter choice (1-6): ")

        if not validate_menu_choice(choice):
            print("Error: Please enter a number between 1 and 6")
            continue

        if choice == 1:
            add_task_ui()
        elif choice == 2:
            view_tasks_ui()
        elif choice == 3:
            update_task_ui()
        elif choice == 4:
            delete_task_ui()
        elif choice == 5:
            toggle_completion_ui()
        elif choice == 6:
            print("\nGoodbye! Your tasks have been cleared from memory.")
            break


if __name__ == "__main__":
    main()
