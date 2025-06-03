#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date

from models.address import Address
from models.person import Person
from models.student import Student
from models.teacher import Teacher
from models.course import Course

def main():
    # Création d'un étudiant avec adresse
    paul = Student('Paul', 'Dubois', 12)
    paul.address = Address('12 rue des Pinsons', 'Castanet', 31320)
    print(paul)  # Affiche : Paul Dubois (12 ans), 12 rue des Pinsons, Castanet 31320

    # Création d'un enseignant
    marie = Teacher('Marie', 'Curie', 31, date(2023, 9, 4))
    marie.address = Address('1 rue des Sciences', 'Paris', 75005)
    print(marie)

    # Création d'un cours
    chimie = Course('Chimie', date(2024, 2, 26), date(2024, 3, 15))

    # Associer le professeur au cours
    chimie.set_teacher(marie)

    # Associer l'étudiant au cours
    chimie.add_student(paul)

    # Affichage info cours
    print(f"Cours : {chimie.name}")
    print(f"Professeur : {chimie.teacher}")
    print("Étudiants inscrits :")
    for student in chimie.students:
        print(f" - {student}")

    # Afficher les cours suivis par Paul
    print(f"\nCours suivis par {paul.first_name} :")
    for course in paul.courses_enrolled:
        print(f" - {course.name} du {course.start_date} au {course.end_date}")

    # Afficher les cours enseignés par Marie
    print(f"\nCours enseignés par {marie.first_name} :")
    for course in marie.courses_taught:
        print(f" - {course.name} du {course.start_date} au {course.end_date}")

if __name__ == '__main__':
    main()
