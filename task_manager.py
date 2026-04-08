def show_tasks(tasks):
    print("\n--- Your Task List ---")
    for i in range(len(tasks)):
        print(i + 1, ".", tasks[i])


n = int(input("How many tasks: "))
tasks = []

for i in range(n):
    task = input("Enter task: ")
    tasks.append(task)

show_tasks(tasks)
