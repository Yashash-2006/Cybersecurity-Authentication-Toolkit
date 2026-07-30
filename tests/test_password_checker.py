import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.password_checker import check_password_strength, calculate_entropy


class TestPasswordChecker(unittest.TestCase):
    """Unit tests for Module 1: Password Strength Checker."""

    def test_common_weak_password(self):
        res = check_password_strength("password")
        self.assertTrue(res["is_common_password"])
        self.assertEqual(res["strength"], "Very Weak (Common Weak Password)")
        self.assertLess(res["score"], 30)

    def test_short_password(self):
        res = check_password_strength("Ab1!")
        self.assertIn("Password is too short", res["recommendations"][0])
        self.assertLessEqual(res["score"], 45)

    def test_strong_password(self):
        res = check_password_strength("Complex#P@ss2026!Secure")
        self.assertFalse(res["is_common_password"])
        self.assertTrue(res["has_uppercase"])
        self.assertTrue(res["has_lowercase"])
        self.assertTrue(res["has_digits"])
        self.assertTrue(res["has_special"])
        self.assertGreaterEqual(res["score"], 80)
        self.assertIn(res["strength"], ["Strong", "Very Strong"])

    def test_entropy_calculation(self):
        entropy = calculate_entropy("abcABC123!@#")
        self.assertGreater(entropy, 50.0)


if __name__ == "__main__":
    unittest.main()
