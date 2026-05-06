todos = []

def add_task(task):
    todos.append(task)
    print("✅ Task added:", task)

def show_tasks():
    if len(todos) == 0:
        print("📭 No tasks yet!")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")

def delete_task(number):
    if number <= len(todos):
        removed = todos.pop(number - 1)
        print("🗑️ Deleted:", removed)
    else:
        print("❌ Task not found!")

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Quit")
    
    choice = input("Choose (1/2/3/4): ")
    
    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        show_tasks()
        num = int(input("Delete task number: "))
        delete_task(num)
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
