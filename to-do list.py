tasks = []
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.\n")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f'"{removed}" deleted successfully!\n')
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")

while True:
    print("====== TO-DO LIST ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.\n")