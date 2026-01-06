"""Task data class for Phase I CLI Todo App.

This module defines the Task class, which represents a single todo item
with an ID, title, description, and completion status.
"""


class Task:
    """Represents a single todo item.

    Attributes:
        id (int): Unique integer identifier
        title (str): Non-empty string describing the task
        description (str): String with optional details (can be empty)
        completed (bool): Boolean completion status
    """

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """Initialize a Task instance.

        Args:
            task_id: Unique integer ID (assigned by TaskManager)
            title: Task title (must be non-empty, validated by TaskManager)
            description: Optional task description (defaults to empty string)
            completed: Completion status (defaults to False)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        """Return string representation of Task for debugging."""
        return (f"Task(id={self.id}, title='{self.title}', "
                f"description='{self.description}', completed={self.completed})")
