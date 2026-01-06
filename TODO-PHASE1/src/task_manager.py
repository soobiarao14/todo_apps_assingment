"""TaskManager class for Phase I CLI Todo App.

This module implements the business logic for managing tasks in memory.
It provides CRUD operations (Create, Read, Update, Delete) and completion toggling.
"""

from task import Task


class TaskManager:
    """Manages in-memory task collection and provides CRUD operations.

    Attributes:
        tasks (list[Task]): List of all tasks in memory
        next_id (int): Counter for generating unique task IDs
    """

    def __init__(self):
        """Initialize TaskManager with empty task list and ID counter starting at 1."""
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> tuple[bool, str]:
        """Add a new task to the task list.

        Args:
            title: Task title (required, must be non-empty)
            description: Task description (optional, defaults to empty string)

        Returns:
            Tuple of (success: bool, message: str)
            - On success: (True, "Task added successfully with ID {id}")
            - On failure: (False, "Task title cannot be empty")
        """
        # Validate title is not empty or whitespace-only
        if not title or not title.strip():
            return (False, "Task title cannot be empty")

        # Create new task with auto-assigned ID
        new_task = Task(
            task_id=self.next_id,
            title=title,
            description=description,
            completed=False
        )

        # Add to list and increment ID counter
        self.tasks.append(new_task)
        task_id = self.next_id
        self.next_id += 1

        return (True, f"Task added successfully with ID {task_id}")

    def view_tasks(self) -> tuple[bool, str]:
        """Retrieve all tasks formatted for display.

        Returns:
            Tuple of (success: bool, message: str)
            - If tasks exist: (True, formatted string with all task details)
            - If no tasks: (True, "No tasks found")
        """
        if not self.tasks:
            return (True, "No tasks found")

        # Format all tasks for display
        lines = []
        for task in self.tasks:
            status = "Complete" if task.completed else "Incomplete"
            lines.append(f"[{task.id}] Title: {task.title}")
            lines.append(f"    Description: {task.description}")
            lines.append(f"    Status: {status}")
            lines.append("")  # Blank line between tasks

        return (True, "\n".join(lines))

    def update_task(self, task_id: int, new_title: str, new_description: str = "") -> tuple[bool, str]:
        """Update an existing task's title and description.

        Args:
            task_id: ID of task to update
            new_title: New title (required, must be non-empty)
            new_description: New description (optional, defaults to empty string)

        Returns:
            Tuple of (success: bool, message: str)
            - On success: (True, "Task updated successfully")
            - On failure: (False, error message)
        """
        # Validate new title is not empty
        if not new_title or not new_title.strip():
            return (False, "Task title cannot be empty")

        # Find task by ID
        task = self._find_task_by_id(task_id)
        if task is None:
            return (False, "Task ID not found")

        # Update task fields
        task.title = new_title
        task.description = new_description

        return (True, "Task updated successfully")

    def delete_task(self, task_id: int) -> tuple[bool, str]:
        """Permanently remove a task from the task list.

        Args:
            task_id: ID of task to delete

        Returns:
            Tuple of (success: bool, message: str)
            - On success: (True, "Task deleted successfully")
            - On failure: (False, "Task ID not found")
        """
        # Find task by ID
        task = self._find_task_by_id(task_id)
        if task is None:
            return (False, "Task ID not found")

        # Remove task from list
        self.tasks.remove(task)

        return (True, "Task deleted successfully")

    def toggle_complete(self, task_id: int) -> tuple[bool, str]:
        """Toggle a task's completion status between complete and incomplete.

        Args:
            task_id: ID of task to toggle

        Returns:
            Tuple of (success: bool, message: str)
            - On success: (True, "Task marked as complete") or (True, "Task marked as incomplete")
            - On failure: (False, "Task ID not found")
        """
        # Find task by ID
        task = self._find_task_by_id(task_id)
        if task is None:
            return (False, "Task ID not found")

        # Toggle completion status
        task.completed = not task.completed

        # Return appropriate message based on new status
        if task.completed:
            return (True, "Task marked as complete")
        else:
            return (True, "Task marked as incomplete")

    def _find_task_by_id(self, task_id: int):
        """Find a task by its ID.

        Args:
            task_id: ID to search for

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
