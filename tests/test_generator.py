import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.password_generator import generate_secure_password
from src.password_checker import check_password_strength


class TestPasswordGenerator(unittest.TestCase):
    """Unit tests for Module 3: Secure Password Generator."""

    def test_generated_length(self):
        pwd = generate_secure_password(length=20)
        self.assertEqual(len(pwd), 20)

    def test_criteria_satisfaction(self):
        pwd = generate_secure_password(length=16, include_upper=True, include_lower=True, include_digits=True, include_special=True)
        eval_res = check_password_strength(pwd)
        self.assertTrue(eval_res["has_uppercase"])
        self.assertTrue(eval_res["has_lowercase"])
        self.assertTrue(eval_res["has_digits"])
        self.assertTrue(eval_res["has_special"])

    def test_no_category_selected(self):
        with self.assertRaises(ValueError):
            generate_secure_password(length=10, include_upper=False, include_lower=False, include_digits=False, include_special=False)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_secure_password(length=2, include_upper=True, include_lower=True, include_digits=True, include_special=True)


if __name__ == "__main__":
    unittest.main()
