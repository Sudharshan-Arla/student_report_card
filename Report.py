class Student:
    def __init__(self, id, name, clss, marks):
        self.id = id
        self.name = name
        self.clss = clss
        self.marks = marks

    def calculate_percentage(self):
        total_marks = 500
        percentage = (self.total_marks_obtained() / total_marks) * 100
        return percentage

    def total_marks_obtained(self):
        total_marks_obtained = 0
        lis_marks = list(self.marks.values())
        for mark in lis_marks:
            total_marks_obtained += mark
        return total_marks_obtained

    def get_grade(self):
        grade = ""
        percentage = self.calculate_percentage()
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80 and percentage < 90:
            grade = "B"
        elif percentage >= 70 and percentage < 80:
            grade = "C"
        else:
            grade = "D"
        return grade

    def get_report_card(self):
        report_card = {}
        report_card["studentID"] = self.id
        report_card["name"] = self.name
        report_card["class"] = self.clss
        report_card["marks"] = self.marks
        report_card["total"] = self.total_marks_obtained()
        report_card["percentage"] = self.calculate_percentage()
        report_card["grade"] = self.get_grade()
        return report_card


name = input("enter student name: ")
clss = int(input("enter the class: "))
math = int(input(" enter math marks: "))
science = int(input(" enter science marks: "))
english = int(input(" enter english marks: "))
history = int(input(" enter history marks: "))
computer = int(input(" enter computer marks: "))

marks = {}
marks["math"] = math
marks["science"] = science
marks["english"] = english
marks["history"] = history
marks["computer"] = computer


student1 = Student(1, name, clss, marks)
print(student1.get_report_card())
