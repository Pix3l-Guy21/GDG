def edit_task(tasks):
    print("Editing existing task")
    task_edit_id = input("Enter the id of the task to edit: ")
    if not tasks.__contains__(task_edit_id):
        print("Invalid id")
        edit_task()
        return
    selected = tasks[task_edit_id]
    edit_option = input("If you want to edit the title enter 't' or to edit the status enter 's': ")
    if edit_option == 's':
        edited_status = input("enter the new status: ")
        print(selected.update(selected.title, edited_status))
    elif edit_option == 't':
        edited_title = input("enter new title: ")
        print(selected.update(edited_title, selected.status))
    else:
        print("incorrect input")