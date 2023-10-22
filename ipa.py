import pickle

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"

def add_task(task_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = Task(title, description)
    task_list.append(task)
    print("Task added successfully!")

def display_tasks(task_list):
    if not task_list:
        print("No tasks to display.")
    else:
        for i, task in enumerate(task_list, 1):
            print(f"Task {i}:\n{task}\n")

def mark_completed(task_list):
    display_tasks(task_list)
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(task_list):
            task_list[task_num].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task(task_list):
    display_tasks(task_list)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(task_list):
            deleted_task = task_list.pop(task_num)
            print(f"Task deleted:\n{deleted_task}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def save_tasks(task_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(task_list, file)
        print(f"Tasks saved to {filename}.")

def load_tasks(filename):
    try:
        with open(filename, 'rb') as file:
            task_list = pickle.load(file)
            print(f"Tasks loaded from {filename}.")
            return task_list
    except FileNotFoundError:
        print("File not found. No tasks loaded.")
        return []

def main():
    tasks = []
    filename = "tasks.pkl"

    while True:
        print("\nTask Management System Menu:")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Save tasks to a file")
        print("6. Load tasks from a file")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks, filename)
        elif choice == '6':
            tasks = load_tasks(filename)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

if __name__ == "__main__":
    main()
