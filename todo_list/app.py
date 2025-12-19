import json
tasks = {}
class Tasks:

    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status
    
    def view(self):
        return {
            "id":self.id,
           "title":self.title,
            "status":self.status
        }
    
    def update(self, new_title, new_status):
        self.title = new_title
        self.status = new_status
        self.save()
        return "task updated"
    
    def save(self):
        global tasks
        tasks[str(self.id)] = self
        self.write_to_json()
        return "task saved"
    
    def write_to_json(self):
        global tasks
        try:
            json_data = {key: obj.view() for key, obj in tasks.items()}
            with open('todos.json', 'w') as file:
                file.write(json.dumps(json_data))
        except:
            print("failed to update and close")

    def delete(self):
        global tasks
        tasks.pop(str(self.id))
        self.write_to_json()
        return "task deleted"

def app_opened():
    try:
        global tasks
        with open('todos.json', 'r') as file:
            raw_data = json.load(file)
        print("Current tasks in the todo list")
        tasks = {}
        for key, val in raw_data.items():
            task_obj = Tasks(val["id"], val["title"], val["status"])
            tasks[key] = task_obj
            print(f'-----------------------------\ntask id: {task_obj.id}\ntitle: {task_obj.title}\nstatus: {task_obj.status}\n-----------------------------')
        print()
    except:
        print("No todo list found")

def running():
    app_opened()
    option = int(input("Enter '1' to add new task\nEnter '2' to update existing tasks\nEnter '3' to delete task\nEnter '4' to exit\n"))
    if option == 1:
        add_new_task()
        return running()
    elif option == 2:
        edit_task()
        return running()
    elif option == 3:
        delete_task()
        return running()
    elif option == 4:
        return

def add_new_task():
    print("Enter task details")
    new_task_id = int(input("Enter new task id: "))
    new_task_title = input("Enter new task title: ")
    new_task_status = "Started"
    task = Tasks(new_task_id, new_task_title, new_task_status)
    print(task.save())

def edit_task():
    global tasks
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

def delete_task():
    global tasks
    print("Deleting task")
    task_delete_id = input("Enter the id of the task to delete: ")
    if not tasks.__contains__(task_delete_id):
        print("Invalid id")
        delete_task()
        return
    tasks[task_delete_id].delete()

#running segment   
print("         ********************************************")
print("                 Hello, this is a todo app cli")
print("         ********************************************")

running()
