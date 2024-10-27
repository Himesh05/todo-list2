# todo_list.py

def add_task(task, todo_list):
    todo_list.append(task)
    print(f'Task "{task}" added!')

def remove_task(task, todo_list):
    if task in todo_list:
        todo_list.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print(f'Task "{task}" not found!')

def display_tasks(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def todo_list():
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            add_task(task, todo_list)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            remove_task(task, todo_list)
        elif choice == '3':
            display_tasks(todo_list)
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid input! Please try again.")

if __name__ == "__main__":
    todo_list()
