#!/usr/bin/python3
import requests
import sys

# Function to fetch and display TODO list progress for a given employee ID
def get_employee_todo_progress(employee_id):
    # Endpoint URL for the REST API
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Send GET request to fetch TODO list data
    response = requests.get(url)

    # Check if response is successful (status code 200)
    if response.status_code == 200:
        # Parse response data as JSON
        todos = response.json()

        # Extract relevant information
        employee_name = todos[0]['username']
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)

        # Display employee TODO list progress
        print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"     {task['title']}")
    else:
        print("Error fetching TODO list data. Please check the employee ID.")

# Accept employee ID as input parameter
if len(sys.argv) == 2:
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
else:
    print("Usage: python3 gather_data_from_an_API.py [EMPLOYEE_ID]")


