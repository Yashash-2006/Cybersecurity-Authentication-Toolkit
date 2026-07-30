"""
Module 5: Password Guessing Detection (by Targeted Username)
--------------------------------------------------------------
Identifies targeted password guessing and dictionary attacks aimed at specific user accounts.
Tracks failed login attempts per username and flags accounts targeted with multiple distinct passwords.
"""

from collections import defaultdict
from typing import List, Dict, Any


def detect_password_guessing_attacks(logs: List[Dict[str, Any]], threshold: int = 3) -> Dict[str, Any]:
    """Analyzes login records to identify user accounts subject to password guessing attacks."""
    user_failed_passwords = defaultdict(set)
    user_failed_attempts_count = defaultdict(int)
    user_source_ips = defaultdict(set)
    user_attempt_timestamps = defaultdict(list)

    total_logs = len(logs)
    total_failures = 0

    for log in logs:
        user = log.get("username") or log.get("user", "unknown")
        ip = log.get("ip_address") or log.get("ip") or log.get("source_ip", "0.0.0.0")
        status = str(log.get("status") or log.get("result", "")).upper()
        password_attempted = log.get("password_attempted") or log.get("password", "<UNSPECIFIED>")
        timestamp = log.get("timestamp", "N/A")

        if status in ("FAILED", "FAILURE", "INVALID"):
            total_failures += 1
            user_failed_attempts_count[user] += 1
            user_failed_passwords[user].add(password_attempted)
            user_source_ips[user].add(ip)
            user_attempt_timestamps[user].append(timestamp)

    flagged_users = []
    for user, passwords_set in user_failed_passwords.items():
        distinct_count = len(passwords_set)
        total_failed = user_failed_attempts_count[user]

        if distinct_count >= threshold:
            flagged_users.append({
                "username": user,
                "total_failed_attempts": total_failed,
                "distinct_passwords_count": distinct_count,
                "passwords_attempted": sorted(list(passwords_set)),
                "source_ips": sorted(list(user_source_ips[user])),
                "timestamps": user_attempt_timestamps[user],
                "attack_type": "Dictionary Attack / Password Spraying",
                "risk_level": "CRITICAL" if distinct_count >= 5 else "HIGH"
            })

    flagged_users.sort(key=lambda x: x["distinct_passwords_count"], reverse=True)

    return {
        "total_logs_processed": total_logs,
        "total_failed_attempts": total_failures,
        "threshold_applied": threshold,
        "targeted_users_flagged": len(flagged_users),
        "flagged_accounts": flagged_users,
        "user_summary": {
            user: {
                "total_failed": user_failed_attempts_count[user],
                "distinct_passwords": len(user_failed_passwords[user])
            }
            for user in user_failed_attempts_count
        }
    }
