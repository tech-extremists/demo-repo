
tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task added: {task}")
    
def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
def list_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i + 1}. {task['task']} [{status}]")
        
def mark_done():
    list_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter task number to mark as done: "))
        tasks[task_num - 1]["done"] = True
        print(f"Task {task_num} marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    print("Welcome to the To-Do List Application")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
