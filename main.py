import csv
import task
import deadline
import os


def read_deadlines(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            deadline.Deadline.csv_row(row)


def read_tasks(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            task.list_of_tasks.append(task.Task.csv_row(row))


def print_deadlines():
    clear_terminal()
    a = 0
    for x in deadline.list_of_deadlines:
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
                if 0 <= index <= len(deadline.list_of_deadlines):
                    break
            except ValueError:
                print('incorrect value')
        delete_deadline(index)
        print_deadlines()


def delete_deadline(a):
    deadline.list_of_deadlines.pop(a)


def delete_task(a):
    task.list_of_tasks.pop(a)


def print_tasks():
    clear_terminal()
    a = 0
    for x in task.list_of_tasks:
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
                if 0 <= index <= len(task.list_of_tasks):
                    break
            except ValueError:
                print('incorrect value')
        delete_task(index)


def starting():
    while True:
        try:
            create_obj = input("1. create deadline \n"
                               "2. create task \n"
                               "3. show all deadlines \n"
                               "4. show all tasks \n")
            if create_obj == '1' or create_obj == '2' or create_obj == '3' or create_obj == '4':
                break
        except ValueError:
            print("type 1 or 2")

    clear_terminal()

    if create_obj == '1':
        deadline.Deadline.save_to_csv(deadline.Deadline.create_deadline(), "deadlines")
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

read_tasks("tasks")
read_deadlines('deadlines')
starting()
