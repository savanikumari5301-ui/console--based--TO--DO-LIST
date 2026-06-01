#IMPLEMENT A SIMPLE TO DO LIST APPLICATION IN PYTHON.
import sys

def show_menu():
    print("\n" + "="*30)
    print("      TO-DO LIST MANAGER      ")
    print("="*30)
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")
    print("="*30)

def view_tasks(tasks):
    if not tasks:
        print("\n[!] Your to-do list is empty.")
        return
    
    print("\n--- YOUR TASKS ---")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("\nEnter the task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print(f"[+] Task '{title}' added successfully!")
    else:
        print("[!] Task description cannot be empty.")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            if tasks[choice - 1]["completed"]:
                print("[!] This task is already marked as completed.")
            else:
                tasks[choice - 1]["completed"] = True
                print(f"[✓] Task '{tasks[choice - 1]['title']}' marked as completed!")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        choice = int(input("\nEnter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"[-] Task '{removed['title']}' deleted successfully.")
        else:
            print("[!] Invalid task number.")
    except ValueError:
        print("[!] Please enter a valid number.")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nThank you for using To-Do List Manager. Goodbye!")
            sys.exit()
        else:
            print("[!] Invalid selection. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
