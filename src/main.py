"""
Cybersecurity Authentication Toolkit - Main CLI Driver
------------------------------------------------------
Course: Python for Cybersecurity
Provides a Rich interactive text-based interface to demonstrate all 5 cybersecurity modules,
parse CSV and JSON authentication logs, run security audits, and execute unit tests.
"""

import sys
import os
import unittest

# Path setup for src module imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.password_checker import check_password_strength
from src.login_lockout import LoginLockoutSimulator
from src.password_generator import generate_and_evaluate_password
from src.brute_force_detector import detect_brute_force_attacks
from src.password_guess_detector import detect_password_guessing_attacks
from src.utils import load_json_logs, load_csv_logs, HAS_RICH

if HAS_RICH:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.prompt import Prompt
    from rich.text import Text
    from rich import print as rprint
    console = Console()
else:
    console = None


SAMPLE_JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "sample_data", "sample_login_logs.json")
SAMPLE_CSV_IP_PATH = os.path.join(os.path.dirname(__file__), "..", "sample_data", "login_attempts.csv")
SAMPLE_CSV_PASS_PATH = os.path.join(os.path.dirname(__file__), "..", "sample_data", "password_attempts.csv")


def load_dataset() -> list:
    """Loads authentication dataset, prioritizing CSV / JSON files."""
    if os.path.exists(SAMPLE_JSON_PATH):
        return load_json_logs(SAMPLE_JSON_PATH)
    elif os.path.exists(SAMPLE_CSV_IP_PATH):
        return load_csv_logs(SAMPLE_CSV_IP_PATH)
    else:
        return [
            {"ip_address": "192.168.1.105", "username": "admin", "status": "FAILED", "password_attempted": "123456"},
            {"ip_address": "192.168.1.105", "username": "admin", "status": "FAILED", "password_attempted": "root"},
            {"ip_address": "192.168.1.105", "username": "admin", "status": "FAILED", "password_attempted": "admin123"},
            {"ip_address": "10.0.0.50", "username": "victim_user", "status": "FAILED", "password_attempted": "pass1"},
            {"ip_address": "10.0.0.50", "username": "victim_user", "status": "FAILED", "password_attempted": "pass2"},
            {"ip_address": "10.0.0.50", "username": "victim_user", "status": "FAILED", "password_attempted": "pass3"},
        ]


def display_menu():
    """Renders the main interactive menu."""
    if HAS_RICH and console:
        console.clear()
        menu_text = Text()
        menu_text.append("============================================\n", style="bold cyan")
        menu_text.append("      Cybersecurity Authentication Toolkit   \n", style="bold white on blue")
        menu_text.append("============================================\n\n", style="bold cyan")
        menu_text.append(" [1] Password Strength Checker\n", style="bold green")
        menu_text.append(" [2] Login Lockout Simulator\n", style="bold green")
        menu_text.append(" [3] Secure Password Generator\n", style="bold green")
        menu_text.append(" [4] Brute Force Detection (by IP)\n", style="bold green")
        menu_text.append(" [5] Password Guessing Detection (by User)\n", style="bold green")
        menu_text.append(" [6] Run Full Automated Security Audit\n", style="bold yellow")
        menu_text.append(" [7] Run Unit Test Suite\n", style="bold magenta")
        menu_text.append(" [0] Exit\n\n", style="bold red")
        menu_text.append("============================================", style="bold cyan")
        
        console.print(Panel(menu_text, border_style="cyan", expand=False))
    else:
        print("\n============================================")
        print("      Cybersecurity Authentication Toolkit")
        print("============================================")
        print(" [1] Password Strength Checker")
        print(" [2] Login Lockout Simulator")
        print(" [3] Secure Password Generator")
        print(" [4] Brute Force Detection (by IP)")
        print(" [5] Password Guessing Detection (by User)")
        print(" [6] Run Full Automated Security Audit")
        print(" [7] Run Unit Test Suite")
        print(" [0] Exit")
        print("============================================\n")


def run_module_1():
    """Module 1 UI Handler."""
    if HAS_RICH and console:
        console.print(Panel("[bold cyan]MODULE 1: PASSWORD STRENGTH CHECKER[/bold cyan]", border_style="cyan"))
        pwd = Prompt.ask("Enter password to evaluate", default="P@ssw0rd2026!Secured")
    else:
        pwd = input("Enter password to evaluate [default: P@ssw0rd2026!Secured]: ").strip() or "P@ssw0rd2026!Secured"

    res = check_password_strength(pwd)

    if HAS_RICH and console:
        table = Table(title=f"Strength Analysis for '{pwd}'", border_style="cyan")
        table.add_column("Metric", style="bold yellow")
        table.add_column("Value", style="bold white")

        table.add_row("Password Length", str(res["password_length"]))
        table.add_row("Overall Score", f"{res['score']} / 100")
        table.add_row("Strength Rating", f"[bold green]{res['strength']}[/bold green]" if res["score"] >= 70 else f"[bold red]{res['strength']}[/bold red]")
        table.add_row("Shannon Entropy", f"{res['entropy_bits']} bits")
        table.add_row("Has Uppercase (A-Z)", "YES" if res["has_uppercase"] else "NO")
        table.add_row("Has Lowercase (a-z)", "YES" if res["has_lowercase"] else "NO")
        table.add_row("Has Digits (0-9)", "YES" if res["has_digits"] else "NO")
        table.add_row("Has Special (!@#$)", "YES" if res["has_special"] else "NO")
        table.add_row("Known Common Weak", "[bold red]YES[/bold red]" if res["is_common_password"] else "NO")

        console.print(table)
        console.print("\n[bold yellow]Security Feedback & Recommendations:[/bold yellow]")
        for rec in res["recommendations"]:
            console.print(f"  • {rec}")
    else:
        print(f"\nPassword: {pwd}")
        print(f"Score: {res['score']}/100 | Strength: {res['strength']} | Entropy: {res['entropy_bits']} bits")
        print("Recommendations:")
        for rec in res["recommendations"]:
            print(f"  • {rec}")


def run_module_2():
    """Module 2 UI Handler."""
    if HAS_RICH and console:
        console.print(Panel("[bold cyan]MODULE 2: LOGIN LOCKOUT SIMULATOR[/bold cyan]", border_style="cyan"))
        console.print("Default Credentials: Username='admin', Password='SecurePass123!'\nMax Attempts Allowed: 3\n")
    else:
        print("\n--- MODULE 2: LOGIN LOCKOUT SIMULATOR ---")

    sim = LoginLockoutSimulator(predefined_user="admin", predefined_pass="SecurePass123!", max_attempts=3)

    while not sim.is_locked:
        if HAS_RICH and console:
            u = Prompt.ask("Username")
            p = Prompt.ask("Password", password=True)
        else:
            u = input("Username: ").strip()
            p = input("Password: ").strip()

        res = sim.attempt_login(u, p)
        if HAS_RICH and console:
            if res["success"]:
                console.print(f"[bold green]{res['message']}[/bold green]")
                break
            else:
                color = "red" if res["is_locked"] else "yellow"
                console.print(f"[{color}]{res['message']}[/{color}]")
        else:
            print(f">> {res['message']}")
            if res["success"]:
                break

    if sim.is_locked:
        if HAS_RICH and console:
            console.print(Panel("[bold red]LOCKOUT ENFORCEMENT ACTIVE![/bold red]\nAttempting login while locked:", border_style="red"))
            lock_test = sim.attempt_login("admin", "any_pass")
            console.print(f"[bold red]{lock_test['message']}[/bold red]")
        else:
            print("\n[!] ACCOUNT LOCKED. Attempting login while locked:")
            print(sim.attempt_login("admin", "any_pass")["message"])


def run_module_3():
    """Module 3 UI Handler."""
    if HAS_RICH and console:
        console.print(Panel("[bold cyan]MODULE 3: SECURE PASSWORD GENERATOR[/bold cyan]", border_style="cyan"))
        length = int(Prompt.ask("Desired Password Length", default="16"))
    else:
        print("\n--- MODULE 3: SECURE PASSWORD GENERATOR ---")
        length = int(input("Desired Length [default 16]: ").strip() or "16")

    res = generate_and_evaluate_password(length, True, True, True, True)

    if HAS_RICH and console:
        table = Table(title="Generated Secure Password Results", border_style="green")
        table.add_column("Property", style="bold cyan")
        table.add_column("Value", style="bold white")
        table.add_row("Generated Password", f"[bold green]{res['generated_password']}[/bold green]")
        table.add_row("Length", str(res["length"]))
        table.add_row("Evaluated Score", f"{res['strength_evaluation']['score']}/100")
        table.add_row("Strength Rating", res["strength_evaluation"]["strength"])
        table.add_row("Entropy", f"{res['strength_evaluation']['entropy_bits']} bits")
        console.print(table)
    else:
        print(f"\nGenerated Password: {res['generated_password']}")
        print(f"Score: {res['strength_evaluation']['score']}/100 | Strength: {res['strength_evaluation']['strength']}")


def run_module_4():
    """Module 4 UI Handler."""
    logs = load_dataset()
    results = detect_brute_force_attacks(logs, threshold=3)

    if HAS_RICH and console:
        console.print(Panel("[bold cyan]MODULE 4: BRUTE-FORCE ATTACK DETECTION (BY IP)[/bold cyan]", border_style="cyan"))
        table = Table(title=f"Flagged Suspicious IP Addresses (Threshold >= 3)", border_style="red")
        table.add_column("IP Address", style="bold red")
        table.add_column("Failed Attempts", style="bold yellow")
        table.add_column("Risk Level", style="bold magenta")
        table.add_column("Targeted Accounts", style="bold white")

        for item in results["flagged_ips"]:
            table.add_row(item["ip_address"], str(item["failed_attempts"]), item["risk_level"], ", ".join(item["targeted_users"]))

        console.print(table)
        console.print(f"\nTotal Logs Processed: {results['total_logs_processed']} | Flagged IPs: {results['suspicious_ip_count']}")
    else:
        print("\n--- MODULE 4: BRUTE FORCE DETECTION ---")
        print(f"Flagged IPs ({results['suspicious_ip_count']}):")
        for item in results["flagged_ips"]:
            print(f"  IP: {item['ip_address']} | Failed Tries: {item['failed_attempts']} | Targeted: {', '.join(item['targeted_users'])}")


def run_module_5():
    """Module 5 UI Handler."""
    logs = load_dataset()
    results = detect_password_guessing_attacks(logs, threshold=3)

    if HAS_RICH and console:
        console.print(Panel("[bold cyan]MODULE 5: PASSWORD GUESSING DETECTION (BY TARGETED USER)[/bold cyan]", border_style="cyan"))
        table = Table(title="Flagged Targeted User Accounts (Threshold >= 3 Distinct Passwords)", border_style="magenta")
        table.add_column("Targeted User", style="bold magenta")
        table.add_column("Total Failed", style="bold yellow")
        table.add_column("Distinct Passwords", style="bold red")
        table.add_column("Sample Passwords Attempted", style="bold white")
        table.add_column("Source IPs", style="bold cyan")

        for item in results["flagged_accounts"]:
            pwds = ", ".join([f"'{p}'" for p in item["passwords_attempted"][:4]])
            table.add_row(item["username"], str(item["total_failed_attempts"]), str(item["distinct_passwords_count"]), pwds, ", ".join(item["source_ips"]))

        console.print(table)
        console.print(f"\nTotal Logs Processed: {results['total_logs_processed']} | Targeted Users Flagged: {results['targeted_users_flagged']}")
    else:
        print("\n--- MODULE 5: PASSWORD GUESSING DETECTION ---")
        print(f"Targeted Accounts Flagged ({results['targeted_users_flagged']}):")
        for item in results["flagged_accounts"]:
            print(f"  User: {item['username']} | Distinct Passwords: {item['distinct_passwords_count']} | IPs: {', '.join(item['source_ips'])}")


def run_full_security_audit():
    """Executes all 5 modules in sequence."""
    if HAS_RICH and console:
        console.print(Panel("[bold gold1]RUNNING AUTOMATED CYBERSECURITY AUTHENTICATION AUDIT[/bold gold1]", border_style="gold1"))
    else:
        print("\n================ RUNNING FULL AUTOMATED AUDIT ================")

    run_module_1()
    run_module_2()
    run_module_3()
    run_module_4()
    run_module_5()


def run_unit_tests():
    """Executes unittest suite."""
    if HAS_RICH and console:
        console.print(Panel("[bold magenta]EXECUTING UNIT TEST SUITE[/bold magenta]", border_style="magenta"))
    else:
        print("\n================ RUNNING UNIT TESTS ================")

    loader = unittest.TestLoader()
    suite = loader.discover(os.path.join(os.path.dirname(__file__), "..", "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


def main():
    """Main CLI Menu Loop."""
    while True:
        display_menu()
        if HAS_RICH and console:
            choice = Prompt.ask("Select an option", choices=["0", "1", "2", "3", "4", "5", "6", "7"])
        else:
            choice = input("Select an option (0-7): ").strip()

        if choice == "1":
            run_module_1()
        elif choice == "2":
            run_module_2()
        elif choice == "3":
            run_module_3()
        elif choice == "4":
            run_module_4()
        elif choice == "5":
            run_module_5()
        elif choice == "6":
            run_full_security_audit()
        elif choice == "7":
            run_unit_tests()
        elif choice == "0":
            if HAS_RICH and console:
                console.print("\n[bold red]Exiting Cybersecurity Authentication Toolkit. Stay Secure![/bold red]\n")
            else:
                print("\nExiting Cybersecurity Authentication Toolkit. Stay Secure!\n")
            sys.exit(0)

        if HAS_RICH and console:
            Prompt.ask("\n[italic dim]Press Enter to return to main menu...[/italic dim]", default="")
        else:
            input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()
