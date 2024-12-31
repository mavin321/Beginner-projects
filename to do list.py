import json


def display_menu():
    print("==========To do list==========")
    print(         "1-Add tasks"          )
    print(         "2-Delete task"        )
    print(         "3-View tasks"         )
    print(         "4-Mark as completed"  )
    print(         "5-Exit"               )
    print("==============================")
tasks=[]


def add_tasks():
    description=input("Enter the description: ")
    due_date=input("enter due date(DD/MM/YYYY): ")
    if due_date== "" :
        due_date=None
    tasks.append({"description": description,
                  "due_date": due_date,
                  "status": "pending"
                  }
                 )
    print("task added successfully!")


def delete_tasks():
    view_tasks()
    if not tasks:
        return
    try:
        task_num=int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            delete_tasks = tasks.pop(task_num-1)
            print(f"task {delete_tasks['description']} Deleted!")
        else:
            print("invalid input")
    except ValueError:
        print("please enter a valid number")





def mark_as_completed():
    view_tasks()
    if not tasks:
        return
    try:
        task_num=int(input("Enter a task number to mark as completed: "))
        if 1<= task_num<=len(tasks):
            tasks[task_num - 1]["status"]="completed"
            print("task marked as completed!")
        else:
            print("invalid task number")
    except ValueError:
        print("please put a valid number.")


import _json
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("tasks saved successfully")


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks= json.load(file)
    except FileNotFoundError:
        tasks = []
    print("Tasks loaded successfully")


def view_tasks():
    if not tasks:
        print("there are no tasks to view")
        return

    print("==========your tasks===========")
    for i, task in enumerate(tasks, start=1):
        status=task["status"]
        due_date=task["due_date"] or "No due date"
        print(f"{i}. {task['description']} - Due: {due_date} - status: {status}")
    print("===============================")


def main():
    load_tasks()
    while True:
        display_menu()
        option=input("what would you like to do? ")
        if option=="1":
            add_tasks()
        elif option=="2":
            delete_tasks()
        elif option=="3":
            view_tasks()
        elif option=="4":
            mark_as_completed()
        elif option=="5":
            save_tasks()
            print("Thank you")
            break
        else:
            print("invalid input.Please try again")

if __name__ =="__main__":
    main()
