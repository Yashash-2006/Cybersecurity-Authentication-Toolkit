import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.login_lockout import LoginLockoutSimulator


class TestLoginLockout(unittest.TestCase):
    """Unit tests for Module 2: Login Lockout Simulator."""

    def setUp(self):
        self.sim = LoginLockoutSimulator(predefined_user="admin", predefined_pass="SecurePass123!", max_attempts=3)

    def test_successful_login(self):
        res = self.sim.attempt_login("admin", "SecurePass123!")
        self.assertTrue(res["success"])
        self.assertFalse(res["is_locked"])
        self.assertEqual(res["remaining_attempts"], 3)

    def test_lockout_sequence(self):
        # 1st Failure
        res1 = self.sim.attempt_login("admin", "wrong1")
        self.assertFalse(res1["success"])
        self.assertEqual(res1["remaining_attempts"], 2)

        # 2nd Failure
        res2 = self.sim.attempt_login("admin", "wrong2")
        self.assertFalse(res2["success"])
        self.assertEqual(res2["remaining_attempts"], 1)

        # 3rd Failure -> Locked
        res3 = self.sim.attempt_login("admin", "wrong3")
        self.assertFalse(res3["success"])
        self.assertTrue(res3["is_locked"])
        self.assertEqual(res3["remaining_attempts"], 0)

        # 4th Attempt while locked -> Rejection
        res4 = self.sim.attempt_login("admin", "SecurePass123!")
        self.assertFalse(res4["success"])
        self.assertTrue(res4["is_locked"])
        self.assertIn("LOCKED", res4["message"])

    def test_unlock_account(self):
        for _ in range(3):
            self.sim.attempt_login("admin", "wrong")
        self.assertTrue(self.sim.is_locked)

        self.sim.unlock_account()
        self.assertFalse(self.sim.is_locked)
        self.assertEqual(self.sim.remaining_attempts, 3)


if __name__ == "__main__":
    unittest.main()
