todo_list = []

def show_tasks():
    print("\nYour To-Do List:")
    if not todo_list:
        print(" - No tasks yet.")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

while True:
    print("\nOptions: add / remove / show / exit")
    action = input("Enter action: ").strip().lower()

    if action == 'add':
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added.")

    elif action == 'remove':
        show_tasks()
        try:
            index = int(input("Enter task number to remove: ")) - 1
            removed = todo_list.pop(index)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number.")

    elif action == 'show':
        show_tasks()

    elif action == 'exit':
        break
    else:
        print("Invalid option.")
