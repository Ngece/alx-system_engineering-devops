#!/usr/bin/python3
import requests
import json

# Function to fetch and export TODO list data in JSON format for all employees
def export_all_employees_todo_json():
    # Endpoint URL for the REST API
    url = 'https://jsonplaceholder.typicode.com/users'

    # Send GET request to fetch employee data
    response = requests.get(url)

    # Check if response is successful (status code 200)
    if response.status_code == 200:
        # Parse response data as JSON
        employees = response.json()

        # Initialize dictionary to store employee tasks
        employee_tasks_dict = {}

        # Loop through each employee
        for employee in employees:
            employee_id = employee['id']
            employee_name = employee['username']

            # Fetch TODO list data for current employee
            todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
            todos_response = requests.get(todos_url)

            # Check if response is successful (status code 200)
            if todos_response.status_code == 200:
                # Parse TODO list data as JSON
                todos = todos_response.json()

                # Extract relevant information
                employee_tasks = []
                for task in todos:
                    task_info = {
                        'username': employee_name,
                        'task': task['title'],
                        'completed': task['completed']
                    }
                    employee_tasks.append(task_info)

                # Add employee tasks to dictionary
                employee_tasks_dict[employee_id] = employee_tasks

            else:
                print(f"Error fetching TODO list data for Employee {employee_name}")

        # Export JSON data to file
        file_name = "todo_all_employees.json"
        with open(file_name, 'w') as json_file:
            json.dump(employee_tasks_dict, json_file, indent=4)

        print(f"TODO list data for all employees exported to {file_name}")

    else:
        print("Error fetching employee data.")

# Call the function to fetch and export TODO list data for all employees
export_all_employees_todo_json()


