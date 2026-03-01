# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False


    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")  # <-- add emoji and exact text
# TODO: Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task_desc):
        task = Task(task_desc)
        self.tasks.append(task)
        print(f"Task '{task_desc}' added for user {self.name}")
        return task

    def complete_task(self, task_desc):
        for task in self.tasks:
         if task.title == title:
            task.complete()
            print(f"✅ Task '{task.title}' completed.")  # ensures exact output
            return