#!/usr/bin/python3
import requests
import csv

""" Function to fetch and export TODO list progress to a CSV file for a given employee ID"""
def export_employee_todo_progress(employee_id):
    """ Endpoint URL for the REST API"""
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        employee_name = todos[0]['username']
        completed_tasks = [todo for todo in todos if todo['completed']]
        total_tasks = len(todos)

        data = []
        for task in todos:
            task_data = [employee_id, employee_name, task['completed'], task['title']]
            data.append(task_data)

        filename = f"{employee_id}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            writer.writerows(data)

        print(f"TODO list progress for Employee {employee_name} has been exported to {filename} successfully.")
    else:
        print("Error fetching TODO list data. Please check the employee ID.")

employee_id = input("Enter employee ID: ")

export_employee_todo_progress(employee_id)

