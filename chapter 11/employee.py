class Employee:
    """雇员"""

    def __init__(self, first, name, salary):
        self.first = first
        self.name = name
        self.salary = int(salary)

    def give_raise(self, increase=5000):
        self.salary += increase
        messages = f"{self.first}{self.name}'s salary is {self.salary}"
        return messages


def greet_user():
    print("hello,world!")
