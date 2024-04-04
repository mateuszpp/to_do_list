import csv
import datetime
from typing import Any

list_of_deadlines = []


class Deadline:

    def __getattribute__(self, title: str) -> Any:
        return super().__getattribute__(title)

    def __init__(self, title=None, deadline=None, priority=None):
        if title is not None and deadline is not None and priority is not None:
            self.title = title
            self.deadline = deadline
            self.priority = priority
        else:
            self.title = None
            self.deadline = None
            self.priority = None
        list_of_deadlines.append(self)

    def __str__(self):
        return f" \n Topic: {self.title} \n deadline {str(self.deadline)}"

    def to_list(self):
        return [self.title, self.deadline, self.priority]

    @classmethod
    def create_deadline(cls):
        title = input("provide the title of the deadline\n")
        while True:
            data_input = input("provide the date in format: YYYY-MM-DD: \n")

            try:
                deadline = datetime.datetime.strptime(data_input, "%Y-%m-%d")
                break
            except ValueError:
                print("incorret format, try again")

        while True:
            try:
                val = int(
                    input("give value interpreting priority of the deadline from 1 as lowest and 3 as highest \n"))
                if 1 <= val <= 3:
                    break
            except ValueError:
                print("incorrect format, give number from 1 to 3")
        return cls(title, deadline, val)

    def save_to_csv(deadline, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            deadline.deadline = deadline.deadline.strftime("%Y-%m-%d")
            writer.writerow(deadline.to_list())

    @classmethod
    def csv_row(cls, csv_row):
        title, date, priority = csv_row
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
        return cls(title, date, int(priority))
