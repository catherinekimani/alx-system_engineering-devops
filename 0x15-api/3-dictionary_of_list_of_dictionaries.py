#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
from json import dump
from requests import get


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    my_dict = {}
    for u in users:
        user_id = u.get('id')
        username = u.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        my_dict[user_id] = []
        for task in tasks:
            my_dict[user_id].append(
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                })

        with open('todo_all_employees.json', 'w') as file:
            dump(my_dict, file)
