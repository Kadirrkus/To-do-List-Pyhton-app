
Task List Application

This application is a simple task (to-do) manager that allows you to create, view, edit, and delete tasks from your computer’s command line. In addition, it archives completed tasks in a separate file for later reference.

Features

Add Task:

Standard task addition: Saves the entered task text with the timestamp into Tasks.txt.

Task with deadline: Prompts the user to enter a deadline for the task and validates the format.

List Tasks:

Displays all existing tasks on the screen, each with a task number.

Edit Task:

Users can select a task from the list and update it with new text.

During editing, pressing “q” exits the edit mode and returns to the main menu.

Each update stores the modification timestamp.

Delete Task:

The selected task is removed and archived into CompletedTasks.txt.

This allows you to view deleted/completed tasks later.

Completed Tasks Management:

Completed tasks are stored separately and can be listed or cleared as needed.

Error Handling

Input Validation:

Empty tasks are not allowed; the program shows an error message and stops the operation.

Task selection requires a number; non-numeric input triggers an error message.

Date Format Validation:

When adding a deadline, the input must follow the format %d/%m/%Y %H:%M (e.g., 20/06/2025 14:30).

Invalid formats trigger an error, and the operation is canceled.

File Exception Handling:

If files are missing or cannot be accessed, the application shows a user-friendly error message instead of crashing.

This ensures a stable experience even in unexpected cases.

Retry on Wrong Input:

For edit and delete operations, invalid inputs trigger error messages, and the user is prompted again until a valid choice is entered.

How to Use

Start the Application:

Run the script in any Python-supported environment.

Menu Options:

1: List current tasks.

2: List completed tasks.

3: Add a new task.

4: Add a task with a deadline (date format: DD/MM/YYYY HH:MM).

5: Enter edit mode to update a task (press q to exit edit mode).

6: Delete a task (deleted tasks are archived as completed).

7: Clear the completed tasks list.

8: Exit the application.

User Input:

The application asks for input at each step and validates the data.

In case of invalid entries, the user is notified and asked to try again.

Conclusion

This task manager application is built with modular functions, making it simple and easy to understand. Robust error handling ensures invalid inputs are managed gracefully, improving user experience. With this tool, you can organize your daily tasks and archive completed ones for future reference.