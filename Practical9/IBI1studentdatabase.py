class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.code_portfolio_score = 100
        self.group_project_score = 100
        self.exam_score = 100

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")
    