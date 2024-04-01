import csv
import datetime


class deadline:
    def __init__(self, title=None, deadline=None, priority=None):
        if title is not None and deadline is not None and priority is not None:
            dateformat = "%Y-%m-%d"
            self.title = title
            self.deadline = deadline
            self.priority = priority
        else:
            self.title = None
            self.deadline = None
            self.priority = None

    def __str__(self):
        return f" \n Topic: {self.title} \n deadline {str(self.deadline)}"

    def to_list(self):
        return [self.title, self.deadline, self.priority]

    @classmethod
    def create_deadline(cls):
        title = input("provide the title of the deadline")
        while True:
            data_input = input("provide the date in format: YYYY-MM-DD: ")

            try:
                deadline = datetime.datetime.strptime(data_input, "%Y-%m-%d")
                break
            except ValueError:
                print("incorret format, try again")

        while True:
            try:
                val = int(
                    input("give valuing interpreting priority of the deadline from 1 as lowest and 3 as highest "))
                if 1 <= val <= 3:
                    break
            except ValueError:
                print("incorrect format, give number from 1 to 3")
        return cls(title, deadline, val)

    def save_to_csv(deadline, filename):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(deadline.to_list())


if __name__ == '__main__':
    p1 = deadline.create_deadline()
    deadline.save_to_csv(p1, "deadlines")
    print(p1.deadline.__str__())
