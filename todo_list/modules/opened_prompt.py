import json
def app_opened(Tasks, tasks):
    try:
        with open('todos.json', 'r') as file:
            raw_data = json.load(file)
        print("Current tasks in the todo list")
        for key, val in raw_data.items():
            task_obj = Tasks(val["id"], val["title"], val["status"])
            tasks[key] = task_obj
            print(f'-----------------------------\ntask id: {task_obj.id}\ntitle: {task_obj.title}\nstatus: {task_obj.status}\n-----------------------------')
        print()
    except:
        print("No todo list found")