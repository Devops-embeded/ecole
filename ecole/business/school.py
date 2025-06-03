# -*- coding: utf-8 -*-
from typing import List
from models.student import Student
from models.teacher import Teacher
from models.course import Course


class School:
    def __init__(self) -> None:
        self.students: List[Student] = []
        self.teachers: List[Teacher] = []
        self.courses: List[Course] = []

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def add_teacher(self, teacher: Teacher) -> None:
        self.teachers.append(teacher)

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def display_courses_list(self) -> None:
        print("Liste des cours :")
        for course in self.courses:
            print(course)
            if course.teacher:
                print(f"  Enseignant : {course.teacher}")
            if course.students:
                print("  Étudiants :")
                for student in course.students:
                    print(f"    - {student}")
            else:
                print("  Aucun étudiant inscrit.")
            print()