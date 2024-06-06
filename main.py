import json
import os

TODO_FILE = 'todo_list.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def list_todos(todos):
    if not todos:
        print("No tasks in the todo list.")
        return
    for index, todo in enumerate(todos, start=1):
        status = 'Done' if todo['completed'] else 'Pending'
        print(f"{index}. [{status}] {todo['task']}")

def add_todo():
    task = input("Enter the task: ")
    todos.append({'task': task, 'completed': False})
    save_todos(todos)
    print("Task added.")

def remove_todo():
    list_todos(todos)
    task_num = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_num < len(todos):
        todos.pop(task_num)
        save_todos(todos)
        print("Task removed.")
    else:
        print("Invalid task number.")

def complete_todo():
    list_todos(todos)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(todos):
        todos[task_num]['completed'] = True
        save_todos(todos)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def main():
    global todos
    todos = load_todos()
    
    while True:
        print("\nTodo List Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Complete task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            list_todos(todos)
        elif choice == '2':
            add_todo()
        elif choice == '3':
            remove_todo()
        elif choice == '4':
            complete_todo()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
