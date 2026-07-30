"""
Module 2: Login Lockout Simulator
---------------------------------
Simulates a secure authentication module that enforces an account lockout policy 
after a maximum of 3 failed login attempts.
"""

from typing import Dict, Any


class LoginLockoutSimulator:
    """Simulates user authentication with lockout protections."""

    def __init__(self, predefined_user: str = "admin", predefined_pass: str = "SecurePass123!", max_attempts: int = 3):
        self._username = predefined_user
        self._password = predefined_pass
        self.max_attempts = max_attempts
        self.failed_attempts = 0
        self.is_locked = False

    @property
    def remaining_attempts(self) -> int:
        return max(0, self.max_attempts - self.failed_attempts)

    def attempt_login(self, username_input: str, password_input: str) -> Dict[str, Any]:
        """Validates login credentials and applies lockout policy."""
        if self.is_locked:
            return {
                "success": False,
                "is_locked": True,
                "remaining_attempts": 0,
                "message": "SECURITY ALERT: Account is LOCKED due to multiple failed login attempts. Access Denied."
            }

        if username_input == self._username and password_input == self._password:
            self.failed_attempts = 0
            return {
                "success": True,
                "is_locked": False,
                "remaining_attempts": self.max_attempts,
                "message": f"SUCCESS: Welcome back, {username_input}! Authentication successful."
            }
        else:
            self.failed_attempts += 1
            if self.failed_attempts >= self.max_attempts:
                self.is_locked = True
                return {
                    "success": False,
                    "is_locked": True,
                    "remaining_attempts": 0,
                    "message": f"SECURITY ALERT: Account '{self._username}' has been LOCKED! Maximum failed attempts (3) exceeded."
                }
            else:
                remaining = self.remaining_attempts
                return {
                    "success": False,
                    "is_locked": False,
                    "remaining_attempts": remaining,
                    "message": f"FAILED LOGIN: Invalid username or password. Remaining attempt(s): {remaining}."
                }

    def unlock_account(self) -> None:
        """Administrative reset to unlock account."""
        self.failed_attempts = 0
        self.is_locked = False
