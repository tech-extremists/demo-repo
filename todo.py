def show_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def main():
    print("Welcome to the To-Do List Application")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "5":
            break

if __name__ == "__main__":
    main()
