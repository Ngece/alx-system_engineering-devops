#!/usr/bin/python3
import requests

# Function to fetch TODO list progress for a given employee ID
def get_employee_todo_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    response = requests.get(url)

    if response.status_code == 200
        todos = response.json()

        employee_name = todos[0]['username']
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)

        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print("Error fetching TODO list data. Please check the employee ID.")

employee_id = input("Enter employee ID: ")
get_employee_todo_progress(employee_id)

