def delete_task(tasks):
    print("Deleting task")
    task_delete_id = input("Enter the id of the task to delete: ")
    if not tasks.__contains__(task_delete_id):
        print("Invalid id")
        delete_task()
        return
    tasks[task_delete_id].delete()