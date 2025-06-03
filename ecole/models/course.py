from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
from models import Teacher, Student



@dataclass
class Course:
    name: str
    start_date: date
    end_date: date
    teacher: Optional[Teacher] = None
    students: List[Student] = field(default_factory=list, init=False)

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)
            if self not in student.courses_enrolled:
                student.courses_enrolled.append(self)

    def set_teacher(self, teacher: Teacher) -> None:
        self.teacher = teacher
        if self not in teacher.courses_taught:
            teacher.courses_taught.append(self)