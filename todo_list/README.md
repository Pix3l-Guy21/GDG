# Todo List App

This is a todo task manager. You can view your current tasks, add new tasks, edit existing tasks or delete them.

## Features

- **Command line interface (CLI)** - all user interactions are through command line
- **Database** - all data is stored in a json file
- **Backend** - python with oop paradigm

## Tech Stack

- **Language** - Python
- **Database** - JSON
- **Hosting** - Locally

# Quick start

## Prerequisites

- **Python 3.x**

## Installation

1. Clone the repository to your local machine with the following commands

    ``` cmd
    git clone --filter=blob:none --no-checkout https://github.com/Pix3l-Guy21/GDG.git
    git cd GDG
    git sparse-checkout init
    git sparse-checkout set todo_list
    git checkout
    ```

2. Run the python script from the cloned repository and you are in the app

    ``` cmd
    cd ./todo_list
    python app.py
    ```

## Structure

1. Each task is handled as entity in the Tasks class

    ``` python
    class Tasks:

        def __init__(self, id, title, status):
            self.id = id
            self.title = title
            self.status = status
        ...
    ```

2. User side (CLI) displays are modularized in functions like running(), add_new_task() and etc
3. The action on the tasks are handled by the methods in the Tasks class.

    ``` python
    ...
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
    ...
    ```
