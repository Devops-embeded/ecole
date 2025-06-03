class Course:
    def __init__(self):
        self.students_taking_it = None
        self.teacher = None

    def set_teacher(self, teacher1):
        pass

    def add_student(self, student1):
        pass

class Teacher:
    name: None

    def __init__(self) -> object:
        self.first_name = None
        self.hiring_date = None
        self.name = None
        self.courses_teached = None
    pass

class Student:
    def __init__(self):
        self.courses_taken = None

    pass

class Person:
    pass