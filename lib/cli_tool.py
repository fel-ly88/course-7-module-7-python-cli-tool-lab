# cli_tool.py

import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}

# TODO: Implement function to add a task for a user
def add_task(args):
        username = args.user
        title = args.title
    # - Check if the user exists, if not, create one
        if username not in users:
            users[username] = User(username)
        
        user = users[username]
    # - Create a new Task with the given title
    
        task = Task(title)
        user.tasks.append(task)
        print(f"📌 Task '{title}' added to {username}.")
    # - Add the task to the user's task list


# TODO: Implement function to mark a task as complete
def complete_task(args):
        username = args.user
        title = args.title
        
    # - Look up the user by name
    # - Look up the task by title
        if username not in users:
            print(f"User {username} not found.")
            return
        user = users[username]
    # - Mark the task as complete
    
        for task in user.tasks:
            if task.title == title:
                task.complete()
                return
    # - Print appropriate error messages if not found

        print(f"Task {title} not found for user {username}")
    

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
