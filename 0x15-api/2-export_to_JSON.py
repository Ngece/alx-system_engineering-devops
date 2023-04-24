#!/usr/bin/python3
import requests
import sys
import json

# Function to fetch and export TODO list data in JSON format for a given employee ID
def export_employee_todo_json(employee_id):
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
        employee_tasks = []
        for task in todos:
            task_info = {
                'task': task['title'],
                'completed': task['completed'],
                'username': employee_name
            }
            employee_tasks.append(task_info)

        # Create JSON data
        employee_data = {employee_id: employee_tasks}

        # Export JSON data to file
        file_name = f"{employee_id}.json"
        with open(file_name, 'w') as json_file:
            json.dump(employee_data, json_file, indent=4)

        print(f"TODO list data for Employee {employee_name} exported to {file_name}")
    else:
        print("Error fetching TODO list data. Please check the employee ID.")

# Accept employee ID as input parameter
if len(sys.argv) == 2:
    employee_id = sys.argv[1]
    export_employee_todo_json(employee_id)
else:
    print("Usage: python3 gather_data_from_an_API.py [EMPLOYEE_ID]")


