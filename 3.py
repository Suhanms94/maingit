to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not to_do_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

print("To-Do List Manager")
print("1. Add a task")
print("2. View tasks")
print("3. Quit")

while True:
    choice = input("Enter choice(1/2/3): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid input")
