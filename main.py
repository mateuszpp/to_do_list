import csv
import task
import deadline
import os

list_of_deadlines = []
list_of_tasks = []


def read_deadlines(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            list_of_deadlines.append(deadline.Deadline.csv_row(row))


def read_tasks(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            list_of_tasks.append(task.Task.csv_row(row))


def print_deadlines():
    clear_terminal()
    a = 0
    for x in list_of_deadlines:
        print(f"{a} \t {x}")
        a += 1
    while True:
        try:
            choice = input("to go back press 'b' to delete deadline press 'd'")
            if choice == 'b' or choice == 'd':
                break
        except ValueError:
            print('incorrect value')
    if choice == 'b':
        starting()
    else:
        while True:
            try:
                index = input("give the index of the deadline you want to delete")
                if 0 <= index <= len(list_of_deadlines):
                    break
            except ValueError:
                print('incorrect value')
        delete_deadline(index)


def delete_deadline(a):
    list_of_deadlines.pop(a)


def delete_task(a):
    list_of_tasks.pop(a)


def print_tasks():
    clear_terminal()
    a = 0
    for x in list_of_tasks:
        print(f"{a} \t {x}")
        a += 1
    while True:
        try:
            choice = input("to go back press 'b' to delete task press 'd'")
            if choice == 'b' or choice == 'd':
                break
        except ValueError:
            print('incorrect value')
    if choice == 'b':
        starting()
    else:
        while True:
            try:
                index = input("give the index of the task you want to delete")
                if 0 <= index <= len(list_of_tasks):
                    break
            except ValueError:
                print('incorrect value')
        delete_task(index)


def starting():
    read_tasks("tasks")
    read_deadlines('deadlines')
    while True:
        try:
            create_obj = input("1. create deadline"
                               "2. create task"
                               "3. show all deadlines"
                               "4. show all tasks")
            if create_obj == '1' or create_obj == '2':
                break
        except ValueError:
            print("type 1 or 2")

    clear_terminal()

    if create_obj == '1':
        deadline.Deadline.create_deadline()
        starting()
    if create_obj == '2':
        task.Task.create_task()
        starting()
    if create_obj == '3':
        print_deadlines()
    else:
        print_tasks()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
