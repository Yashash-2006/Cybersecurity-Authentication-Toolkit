import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.brute_force_detector import detect_brute_force_attacks
from src.password_guess_detector import detect_password_guessing_attacks


class TestDetectors(unittest.TestCase):
    """Unit tests for Module 4 (Brute Force IP) & Module 5 (Password Guessing User)."""

    def test_detect_brute_force_ip(self):
        logs = [
            {"ip_address": "192.168.1.50", "username": "user1", "status": "FAILED"},
            {"ip_address": "192.168.1.50", "username": "user2", "status": "FAILED"},
            {"ip_address": "192.168.1.50", "username": "user3", "status": "FAILED"},
            {"ip_address": "192.168.1.99", "username": "user1", "status": "FAILED"},
            {"ip_address": "192.168.1.99", "username": "user1", "status": "SUCCESS"},
        ]
        results = detect_brute_force_attacks(logs, threshold=3)
        self.assertEqual(results["suspicious_ip_count"], 1)
        self.assertEqual(results["flagged_ips"][0]["ip_address"], "192.168.1.50")
        self.assertEqual(results["flagged_ips"][0]["failed_attempts"], 3)

    def test_detect_password_guessing_user(self):
        logs = [
            {"ip_address": "10.0.0.5", "username": "target_acc", "status": "FAILED", "password_attempted": "pass1"},
            {"ip_address": "10.0.0.5", "username": "target_acc", "status": "FAILED", "password_attempted": "pass2"},
            {"ip_address": "10.0.0.5", "username": "target_acc", "status": "FAILED", "password_attempted": "pass3"},
            {"ip_address": "10.0.0.9", "username": "normal_acc", "status": "FAILED", "password_attempted": "same_pass"},
            {"ip_address": "10.0.0.9", "username": "normal_acc", "status": "FAILED", "password_attempted": "same_pass"},
        ]
        results = detect_password_guessing_attacks(logs, threshold=3)
        self.assertEqual(results["targeted_users_flagged"], 1)
        self.assertEqual(results["flagged_accounts"][0]["username"], "target_acc")
        self.assertEqual(results["flagged_accounts"][0]["distinct_passwords_count"], 3)


if __name__ == "__main__":
    unittest.main()
