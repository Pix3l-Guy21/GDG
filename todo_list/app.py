import json
from modules import delete_prompt, opened_prompt, add_new_prompt, edit_prompt
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

def running():
    opened_prompt.app_opened(Tasks, tasks)
    option = int(input("Enter '1' to add new task\nEnter '2' to update existing tasks\nEnter '3' to delete task\nEnter '4' to exit\n"))
    if option == 1:
        add_new_prompt.add_new_task(Tasks)
        return running()
    elif option == 2:
        edit_prompt.edit_task(tasks)
        return running()
    elif option == 3:
        delete_prompt.delete_task(tasks)
        return running()
    elif option == 4:
        return

#running segment   
print("         ********************************************")
print("                 Hello, this is a todo app cli")
print("         ********************************************")

running()
