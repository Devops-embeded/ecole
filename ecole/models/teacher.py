from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import List
from .person import Person
from .course import Course


@dataclass
class Teacher(Person):
    hire_date: date
    courses_taught: List[Course] = field(default_factory=list, init=False)

    def add_course(self, course: Course) -> None:
        if course not in self.courses_taught:
            self.courses_taught.append(course)
            course.set_teacher(self)

