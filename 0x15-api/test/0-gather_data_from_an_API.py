#!/usr/bin/python3

import requests
import sys


if __name__ == '__main__':
    employedId = sys.argv[1];
    baseUrl = "https://jsonplaceholder.typicode.com/users"

    url = baseUrl + '/' + employedId;
    response = requests.get(url);
    employeeName = response.json().get('name');

    todoUrl = url + '/todos';
    response = requests.get(todoUrl);
    tasks = response.json();

    done = 0;
    doneTask = [];

    for task in tasks:
        if task.get('completed'):
            doneTask.append(tasks);
            print(tasks);
            done += 1;

    #print("Employee {} is done with tasks({}/{}):".format(employeeName, done, len(tasks)));


