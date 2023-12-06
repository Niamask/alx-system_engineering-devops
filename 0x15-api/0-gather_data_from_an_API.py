#!/usr/bin/python3
"""module to fetch URL"""

if __name__ == "__main__":
    import requests
    import sys
    num = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(num)
    response = requests.get(api_url)
    dicti = response.json()
    todoTask = []
    tasks = 0
    for todo in dicti:
        tasks = tasks + 1
        if todo["completed"] is True:
            todoTask.append(todo["title"])
    api_url = "https://jsonplaceholder.typicode.com/users/{}".format(num)
    response = requests.get(api_url)
    name = response.json()["name"]
    tot = len(todoTask)
    print("Employee {} is done with tasks({}/{}):".format(name, tot, tasks))
    for item in todoTask:
        print("\t {}".format(item))
