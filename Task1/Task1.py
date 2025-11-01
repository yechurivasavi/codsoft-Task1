# ---------------Simple To Do List Application ----------
def show_tasks(tasks):
    if tasks:
        print("Your tasks:")
        for task in tasks:
            print(f"\t- {task}")
    else:
        print("There is no task in the list")


def add_task(tasks: list):
    task = input("Enter a task:")
    # tasks.append(task)
    tasks.append(task.lower())


def remove_task(tasks: list):
    # task = input("Enter a task to remove:")
    task = input("Enter a task to remove:").lower()
    if task in tasks:
        tasks.remove(task)
        print(f"--{task} is removed from the list")
    else:
        print(f"--{task} is not found in the list")


tasks = []  # create an empty list

while True:
    print("----To-Do List----")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    option = input("Choose an option:")

    if option == "1":
        show_tasks(tasks)
    elif option == "2":
        add_task(tasks)
    elif option == "3":
        remove_task(tasks)
    elif option == "4":
        break
    else:
        print("You selected an invalid option")