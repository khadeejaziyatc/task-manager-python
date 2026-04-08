
tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted")
            else:
                print("Invalid number")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to update")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated")
            else:
                print("Invalid number")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
