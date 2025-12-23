def add_new_task(Tasks):
    print("Enter task details")
    new_task_id = int(input("Enter new task id: "))
    new_task_title = input("Enter new task title: ")
    new_task_status = "Started"
    task = Tasks(new_task_id, new_task_title, new_task_status)
    print(task.save())
