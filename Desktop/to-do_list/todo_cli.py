def display_todo_list(tasks):
    print("=" * 40)
    print("        Today's To-Do List")
    print("=" * 40)

    sections = {
        "Morning Tasks": [],
        "Afternoon Tasks": [],
        "Evening Tasks": []
    }

    for task in tasks:
        sections[task["time_of_day"]].append(task)

    for section_name, section_tasks in sections.items():
        print(f"\n--- {section_name} ---")
        if not section_tasks:
            print("  No tasks for this section.")
        else:
            for i, task in enumerate(section_tasks):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{status} {task['description']} (Priority: {task['priority']})")

if __name__ == "__main__":
    # Example tasks
    todo_tasks = [
        {
            "description": "Review project proposal",
            "priority": "High",
            "completed": False,
            "time_of_day": "Morning Tasks"
        },
        {
            "description": "Send daily stand-up email",
            "priority": "Medium",
            "completed": True,
            "time_of_day": "Morning Tasks"
        },
        {
            "description": "Attend team meeting",
            "priority": "High",
            "completed": False,
            "time_of_day": "Afternoon Tasks"
        },
        {
            "description": "Work on feature X",
            "priority": "High",
            "completed": False,
            "time_of_day": "Afternoon Tasks"
        },
        {
            "description": "Plan tomorrow's tasks",
            "priority": "Low",
            "completed": False,
            "time_of_day": "Evening Tasks"
        },
        {
            "description": "Read technical article",
            "priority": "Medium",
            "completed": True,
            "time_of_day": "Evening Tasks"
        }
    ]

    display_todo_list(todo_tasks)
