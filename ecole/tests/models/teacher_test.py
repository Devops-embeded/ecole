# tests/models/teacher_test.py
import unittest
from datetime import date
from models.teacher import Teacher  # Correction d'import

class TestTeacher(unittest.TestCase):
    def setUp(self):
        """Méthode d'initialisation pour chaque test"""
        # Création de deux enseignants avec prénom, nom, âge, date d'embauche
        self.teacher1 = Teacher(
            first_name="Jean",
            last_name="Dupont",
            age=42,
            hire_date=date(2022, 9, 1)
        )
        self.teacher2 = Teacher(
            first_name="Marie",
            last_name="Martin",
            age=47,
            hire_date=date(2020, 5, 15)
        )

    def test_teacher_creation(self):
        """Test la création des enseignants"""
        self.assertEqual(self.teacher1.first_name, "Jean")
        self.assertEqual(self.teacher1.last_name, "Dupont")
        self.assertEqual(self.teacher2.first_name, "Marie")
        self.assertEqual(self.teacher2.last_name, "Martin")
        self.assertIsInstance(self.teacher1.hire_date, date)
        self.assertIsInstance(self.teacher2.hire_date, date)

if __name__ == '__main__':
    unittest.main()