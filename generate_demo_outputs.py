"""
Demonstration Script for Submission Screenshots & Audit Records
--------------------------------------------------------------
Executes all 5 cybersecurity modules with structured, visually distinct outputs 
to generate clear demonstration logs ready for screenshot capture.
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.password_checker import check_password_strength
from src.login_lockout import LoginLockoutSimulator
from src.password_generator import generate_and_evaluate_password
from src.brute_force_detector import detect_brute_force_attacks
from src.password_guess_detector import detect_password_guessing_attacks
from src.main import load_dataset
from src.utils import HAS_RICH

if HAS_RICH:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import print as rprint
    console = Console()
else:
    console = None


def run_demo():
    print("=" * 80)
    print("      PYTHON CYBERSECURITY AUTHENTICATION TOOLKIT - DEMONSTRATION RECORD      ")
    print("=" * 80)
    print("Student Submission Execution Log")
    print("Course: Python for Cybersecurity")
    print("=" * 80 + "\n")

    # MODULE 1 DEMO
    print("\n[>>> DEMO SCREENSHOT SECTION 1: MODULE 1 - PASSWORD STRENGTH CHECKER <<<]\n")
    sample_passwords = ["123456", "admin2026", "P@ssw0rd2026!Secured"]
    for pwd in sample_passwords:
        res = check_password_strength(pwd)
        print(f"Password: '{pwd}' (Length: {res['password_length']})")
        print(f"  Score: {res['score']}/100 | Rating: {res['strength']} | Entropy: {res['entropy_bits']} bits")
        print(f"  Recommendations: {', '.join(res['recommendations'])}\n")

    # MODULE 2 DEMO
    print("\n[>>> DEMO SCREENSHOT SECTION 2: MODULE 2 - LOGIN LOCKOUT SIMULATOR <<<]\n")
    sim = LoginLockoutSimulator(predefined_user="admin", predefined_pass="SecurePass123!", max_attempts=3)
    print("Initializing LoginLockoutSimulator (Target User: 'admin', Max Attempts: 3)")
    print("-" * 75)
    
    attempts = [
        ("admin", "wrong_password_1"),
        ("admin", "wrong_password_2"),
        ("admin", "wrong_password_3"),
        ("admin", "SecurePass123!")
    ]

    for idx, (u, p) in enumerate(attempts, 1):
        res = sim.attempt_login(u, p)
        print(f"Step {idx}: Username='{u}', Password='{p}'")
        print(f"       -> Success: {res['success']}, Locked: {res['is_locked']}, Remaining Attempts: {res['remaining_attempts']}")
        print(f"       -> Message: {res['message']}\n")

    # MODULE 3 DEMO
    print("\n[>>> DEMO SCREENSHOT SECTION 3: MODULE 3 - SECURE PASSWORD GENERATOR <<<]\n")
    configs = [
        (12, True, True, True, False, "12 Chars (Upper, Lower, Digits)"),
        (16, True, True, True, True, "16 Chars (All Categories Enabled)"),
        (24, True, True, True, True, "24 Chars (High Entropy Master Password)")
    ]

    for length, u, l, d, s, label in configs:
        res = generate_and_evaluate_password(length, u, l, d, s)
        print(f"Config: {label}")
        print(f"  Generated Password : {res['generated_password']}")
        print(f"  Length: {res['length']} | Score: {res['strength_evaluation']['score']}/100 | Rating: {res['strength_evaluation']['strength']} | Entropy: {res['strength_evaluation']['entropy_bits']} bits\n")

    logs = load_dataset()

    # MODULE 4 DEMO
    print("\n[>>> DEMO SCREENSHOT SECTION 4: MODULE 4 - BRUTE-FORCE ATTACK DETECTION <<<]\n")
    bf_res = detect_brute_force_attacks(logs, threshold=3)
    print(f"Total Logs Processed: {bf_res['total_logs_processed']} | Flagged Suspicious IPs: {bf_res['suspicious_ip_count']}")
    for item in bf_res["flagged_ips"]:
        print(f"  IP: {item['ip_address']} | Failed Attempts: {item['failed_attempts']} | Risk: {item['risk_level']} | Targeted Users: {', '.join(item['targeted_users'])}")

    # MODULE 5 DEMO
    print("\n\n[>>> DEMO SCREENSHOT SECTION 5: MODULE 5 - PASSWORD GUESSING DETECTION <<<]\n")
    pg_res = detect_password_guessing_attacks(logs, threshold=3)
    print(f"Total Logs Processed: {pg_res['total_logs_processed']} | Targeted Users Flagged: {pg_res['targeted_users_flagged']}")
    for item in pg_res["flagged_accounts"]:
        pwds = ", ".join([f"'{p}'" for p in item["passwords_attempted"]])
        print(f"  Target User: {item['username']} | Distinct Passwords Tried: {item['distinct_passwords_count']} | Passwords Sample: {pwds} | Originating IPs: {', '.join(item['source_ips'])}")

    print("\n" + "=" * 80)
    print("                     END OF DEMONSTRATION LOG                        ")
    print("=" * 80)


if __name__ == "__main__":
    run_demo()
