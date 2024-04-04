import csv

list_of_tasks = []


class Task:

    def __init__(self, title=None, priority=None):
        if title is not None and priority is not None:
            self.title = title
            self.priority = priority
        else:
            self.title = None
            self.priority = None
        list_of_tasks.append(self)

    def __str__(self):
            return f" \n Topic: {self.title} "

    def to_list(self):
        return [self.title, self.priority]

    @classmethod
    def create_task(cls):
        title = input("provide the title of the task\n")
        while True:
            try:
                val = int(
                    input("give value interpreting priority of the deadline from 1 as lowest and 3 as highest \n"))
                if 1 <= val <= 3:
                    break
            except ValueError:
                print("incorrect format, give number from 1 to 3")

        while True:
            try:
                daily = int(
                    input("press 1 if it is daily task, else press 0\n"))
                # daily task mean that if you check it as done today it will come back tomorrow as well, other tasks
                # will be deleted immediately
                if daily == '1' or daily == '0':
                    break
            except ValueError:
                print("incorrect format, give number 1 or 0 ")
        return cls(title, val)

    def save_to_csv(task, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(task.to_list())

    @classmethod
    def csv_row(cls, csv_row):
        title, priority = csv_row
        return cls(title, int(priority))
