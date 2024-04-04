import csv
import datetime

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
            task.Task.csv_row(row)


def print_deadlines():
    clear_terminal()
    a = 0
    for x in deadline.list_of_deadlines:
        print(f"{a} \t {x}")
        a += 1



def delete():
    print_deadlines()
    while True:
        try:
            index = input("give the index of the deadline you want to delete\n")
            if 0 <= int(index) <= len(deadline.list_of_deadlines) - 1:
                break
        except ValueError:
            print('incorrect value')
    delete_deadline(int(index), 'deadlines')


def delete_2():
    print_tasks()
    while True:
        try:
            index = input("give the index of the task you want to delete\n")
            if 0 <= int(index) <= len(deadline.list_of_deadlines) - 1:
                break
        except ValueError:
            print('incorrect value')
    delete_task(int(index), 'tasks')


def delete_deadline(a, filename):
    title = deadline.list_of_deadlines[a].title
    date = deadline.list_of_deadlines[a].deadline

    rows_to_keep = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            if row[0] != title or row[1] != date:
                rows_to_keep.append(row)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows_to_keep)

    deadline.list_of_deadlines.pop(a)


def delete_task(a, filename):
    title = task.list_of_tasks[a].title

    rows_to_keep = []
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            if row[0] != title:
                rows_to_keep.append(row)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows_to_keep)

    task.list_of_tasks.pop(a)


def print_tasks():
    clear_terminal()
    a = 0
    for x in task.list_of_tasks:
        print(f"{a} \t {x}")
        a += 1



def starting():
    while True:
        try:
            create_obj = input("\n------------------------\n"
                               "1. create deadline \n"
                               "2. create task \n"
                               "3. show all deadlines \n"
                               "4. show all tasks \n"
                               "5. delete deadline \n"
                               "6.  delete task\n")
            if 1 <= int(create_obj) <= 6:
                break
        except ValueError:
            print("type 1 or 2")

    clear_terminal()

    if create_obj == '1':
        deadline.Deadline.save_to_csv(deadline.Deadline.create_deadline(), "deadlines")
        starting()
    if create_obj == '2':
        task.Task.save_to_csv(task.Task.create_task(), "tasks")
        starting()
    if create_obj == '3':
        print_deadlines()
        starting()
    if create_obj == '4':
        print_tasks()
        starting()
    if create_obj == '5':
        delete()
        starting()
    else:
        delete_2()
        starting()


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


read_tasks("tasks")
read_deadlines('deadlines')
starting()
