# Function to display the menu options
def display_menu():
    print("Menu:")
    print("1. Add Task:")
    print("2. View Task:")
    print("3. Mark as Done:")
    print("4. Exit")



# Function to add new task to the task list
def add_task(tasks):
    task = input("Enter task description: ")    # get the task description to user
    tasks.append(task)  # add task to the list 
    print("Task added successfully!")



# Function to display all task
def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):  # Display task with numbering 
        print(f"{i}. {task}")



# Function to mark a task as done (remove it from the list)
def mark_task_done(tasks):
    if not tasks:  # Check if there are no task
        print("No tasks to mark as Done.")
        return
 
    view_tasks(tasks)    # show task for the user to choose from
    index = int(input("Enter task index to mark as done: ")) - 1  # Get task index from user


    if 0 <= index < len(tasks):  # validate task date
        removed_task = tasks.pop(index)   # Remove task from the list 
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")  # Handle Invalid input



# Function to save task to the file
def save_tasks(tasks):
    with open("tasks.txt" , "w") as f:   # open file in write mode 
        for task in tasks:
            f.write(task + '\n')     # write each task on a new line  



# Function to load the tasks from a file 
def load_tasks():
    try:
        with open("tasks.txt" , "r") as f:  # open the file  in read mode
            return f.read().splitlines()   # Return tasks as a list  of  string 
    except FileNotFoundError:   # if the  file  doesn't exist , return an empty list 
        return[]


# Main function that runs the task manager
def main():
    tasks = load_tasks()  # load previously saved tasks

    while True:
        display_menu()  # show the menu options 

        choice = input("Enter your choice: ")  # Get user's menu choice

        if choice == '1':
            add_task(tasks)   # add a task 
        elif choice == '2':
            view_tasks(tasks)  # View all the task 
        elif choice == '3':
            mark_task_done(tasks)  # mark a task as done
        elif choice == '4':
            print("Exiting.")
            save_tasks(tasks)   # Save tasks to file before exiting 
            break
        else:
            print("Invalid choice. Please select a valid option.")  # handle invalid input 
    
# Run the main function when the script is executed 
if __name__ == "__main__":
    main()