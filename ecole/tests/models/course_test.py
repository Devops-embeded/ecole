import unittest
from datetime import date

from models.teacher import Teacher


class TestTeacher(unittest.TestCase):
    def setUp(self):
        """Méthode d'initialisation pour chaque test"""
        # Création de deux enseignants avec leurs paramètres obligatoires
        self.teacher1 = Teacher(
            first_name="Prof.",
            last_name="Dupont",
            age=45,
            hire_date=date(2022, 9, 1)
        )
        self.teacher2 = Teacher(
            first_name="Prof.",
            last_name="Martin",
            age=50,
            hire_date=date(2020, 5, 15)
        )

    def test_teacher_creation(self):
        """Test la création des enseignants"""
        self.assertEqual(self.teacher1.first_name, "Prof.")
        self.assertEqual(self.teacher1.last_name, "Dupont")
        self.assertEqual(self.teacher2.first_name, "Prof.")
        self.assertEqual(self.teacher2.last_name, "Martin")
        self.assertIsInstance(self.teacher1.hire_date, date)
        self.assertIsInstance(self.teacher2.hire_date, date)

    def test_add_course_does_not_update_courses_taught(self):
        from models.course import Course

        course = Course("Mathématiques", None, None)
        self.teacher1.add_course(course)

        # Ce test doit échouer si add_course ne met pas à jour courses_taught
        self.assertIn(course, self.teacher1.courses_taught)

if __name__ == '__main__':
    unittest.main()