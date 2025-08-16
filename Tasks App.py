## License

# This project was created by **Abdulkadir Kuş**.  
# All rights reserved. The code may not be copied, distributed, or used without explicit permission.


from datetime import datetime
import time

def add_task():
    task = input("Please enter a task: ")
    if not task.strip():
        print("Empty task cannot be added. Try again.")
        return
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("Tasks.txt", "a") as task_list:
        task_list.write(f"{task.strip()}\t(Added on: {timestamp})\n")

def add_task_with_deadline():
    task = input("Please enter a task: ")
    deadline = input("Please enter the deadline (DD/MM/YYYY HH:MM): ")
    if not deadline:
        print("Empty input is not allowed.")
        return
    try:
        datetime.strptime(deadline, "%d/%m/%Y %H:%M")
    except ValueError:
        print("Invalid date format! Please use (DD/MM/YYYY HH:MM).")
        return
    if not task.strip():
        print("Empty task cannot be added. Try again.")
        return
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("Tasks.txt", "a") as task_list:
        task_list.write(f"{task.strip()}\t(Added on: {timestamp}) /// Deadline: {deadline}\n")

def list_tasks():
    print("\n----- Task List -----")
    try:
        with open("Tasks.txt", "r") as task_list:
            tasks = task_list.readlines()
            if not tasks:
                print("No tasks found.")
                return
            for index, line in enumerate(tasks, start=1):
                print(f"{index}. Task: {line.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def edit_task():
    try:
        with open("Tasks.txt", "r") as task_list:
            tasks = task_list.readlines()
        while True:
            if not tasks:
                print("No tasks available to edit.")
                return
            print("\n--------- Task List ---------")
            for index, line in enumerate(tasks, start=1):
                print(f"{index}. Task: {line.strip()}")

            choice = input("\nSelect the task you want to edit.\n(Press q to return to the main menu)>>: ")

            if choice.lower() == "q":
                print("Exiting edit mode...")
                time.sleep(1.2)
                break

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            index = int(choice) - 1
            if index < 0 or index >= len(tasks):
                print("No task found with this number. Try again.")
                continue

            print(tasks[index].strip())
            new_task = input("Enter the updated task:\n")
            if not new_task:
                print("Empty task is not allowed. Try again.")
                continue

            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
            tasks[index] = new_task + f"\t|(Updated on: {timestamp})\n"

            with open("Tasks.txt", "w") as task_list:
                task_list.writelines(tasks)
                print(f"Task {index+1} updated successfully.")

    except FileNotFoundError:
        print("No tasks found.")

def delete_task():
    try:
        with open("Tasks.txt", "r") as task_list:
            tasks = task_list.readlines()

        for index, line in enumerate(tasks, start=1):
            print(f"{index}. Task: {line.strip()}")

        choice = input(f"Enter the number of the task you want to delete (1-{len(tasks)}): ")

        if not choice.isdigit():
            print("Please enter a valid task number.")
            return
        task_no = int(choice) - 1
        if task_no < 0 or task_no >= len(tasks):
            print("No such task found.")
            return

        deleted_task = tasks[task_no].strip()
        with open("CompletedTasks.txt", "a") as completed:
            completed.writelines(deleted_task + "\n")

        del tasks[task_no]
        with open("Tasks.txt", "w") as task_list:
            task_list.writelines(tasks)

        print(f"Task deleted: {deleted_task}")

    except FileNotFoundError:
        print("No tasks found.")

def list_completed_tasks():
    try:
        with open("CompletedTasks.txt", "r") as completed:
            tasks = completed.readlines()
            if not tasks:
                print("No completed tasks found.")
                return
            print("--------- Completed Tasks ---------\n")
            for index, line in enumerate(tasks, start=1):
                print(f"{index}. Task: {line.strip()}")
    except FileNotFoundError:
        print("No completed tasks found.")

def clear_completed_tasks():
    with open("CompletedTasks.txt", "r+") as completed:
        completed.truncate(0)
    print("All completed tasks have been cleared.")


while True:
    print("\n1 - List Tasks")
    print("2 - List Completed Tasks")
    print("3 - Add Task")
    print("4 - Add Task with Deadline")
    print("5 - Edit Task")
    print("6 - Delete Task")
    print("7 - Clear Completed Tasks")
    print("8 - Exit\n")

    choice = input("Please select an option (1-8): ")

    if choice == "1":
        list_tasks()
    elif choice == "2":
        list_completed_tasks()
    elif choice == "3":
        add_task()
    elif choice == "4":
        add_task_with_deadline()
    elif choice == "5":
        edit_task()
    elif choice == "6":
        delete_task()
    elif choice == "7":
        clear_completed_tasks()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")

