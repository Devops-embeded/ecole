from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from .person import Person
from .course import Course



@dataclass
class Student(Person):
    courses_enrolled: List[Course] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        if course not in self.courses_enrolled:
            self.courses_enrolled.append(course)
            course.add_student(self)