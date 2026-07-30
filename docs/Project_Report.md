# Cybersecurity Authentication Toolkit – Technical Report

**Course**: Python for Cybersecurity  
**Assignment Title**: Secure Authentication Toolkit Using Python  
**Author**: Cybersecurity Student  
**Repository Structure**: Standard Python Package (`src/`), Unit Tests (`tests/`), Sample Datasets (`sample_data/`), Interactive CLI (`main.py`)

---

## 1. Executive Summary & Architecture Overview

The **Cybersecurity Authentication Toolkit** is a modular Python application designed to simulate, analyze, and enforce key aspects of modern authentication security and identity threat detection. Built using standard, secure Python 3 libraries (including `secrets`, `string`, `re`, `collections`, `rich`, and `unittest`), the application provides terminal visualizations and security alerts.

The architecture is divided into five core functional modules managed by an interactive CLI driver (`main.py`):
1. **Module 1**: Password Strength Evaluator (Entropy & Heuristics)
2. **Module 2**: Account Login Lockout Simulator
3. **Module 3**: Cryptographically Secure Password Generator (CSPRNG)
4. **Module 4**: IP-Based Brute-Force Attack Detector
5. **Module 5**: Targeted Password Guessing & Spraying Detector

---

## 2. Module Functionality & Technical Design

### Module 1 – Password Strength Checker
- **Functionality**: Evaluates user-supplied passwords against length, character variety (uppercase, lowercase, digits, special symbols), entropy estimation, and known weak pattern checking.
- **Evaluation Criteria**: 
  - Passwords shorter than 8 characters are strictly capped at a max score of 45/100 to reflect real-world vulnerability to rapid brute-forcing.
  - Scores range from 0 to 100 with five discrete strength categories: *Very Weak*, *Weak*, *Moderate*, *Strong*, and *Very Strong*.
  - Calculates Shannon Entropy ($E = L \times \log_2(N)$).

### Module 2 – Login Lockout Simulator
- **Functionality**: Simulates a stateful authentication gateway protecting predefined credentials (`admin` / `SecurePass123!`).
- **Enforcement Mechanics**:
  - Enforces a maximum threshold of **3 failed attempts**.
  - Dynamically computes and displays remaining attempts after each failure.
  - Upon the 3rd consecutive failure, transitions account state to `is_locked = True`.
  - Rejects subsequent login attempts with a security alert message (`SECURITY ALERT: Account is LOCKED...`).

### Module 3 – Secure Password Generator
- **Functionality**: Generates random passwords tailored to user-specified lengths and character inclusions.
- **Security Assurance**:
  - Utilizes Python’s `secrets` module (CSPRNG) instead of pseudo-random generators like `random`.
  - **Guaranteed Category Inclusion**: Explicitly selects at least one random character from *each* enabled category before filling remaining slots.

### Module 4 – Brute-Force Attack Detection (by IP Address)
- **Functionality**: Parses authentication logs to detect host-based brute-force attempts.
- **Detection Logic**:
  - Filters log events where `status == "FAILED"`.
  - Aggregates failure counts grouped by source IP address (`ip_address`).
  - Triggers a security alert for any IP address with $\ge 3$ failed attempts.

### Module 5 – Password Guessing Detection (by Targeted Username)
- **Functionality**: Analyzes logs to distinguish between user typing mistakes and targeted dictionary or password spraying attacks against individual user accounts.
- **Detection Logic**:
  - Grouping by `username` and tracking the set of **distinct failed passwords** attempted (`set()`).
  - Triggers an alert when a single username accumulates $\ge 3$ distinct failed passwords.

---

## 3. Comparative Summary of Attack Detection Modules

| Dimension | Module 4 (Brute Force Detection) | Module 5 (Password Guessing Detection) |
| :--- | :--- | :--- |
| **Focus Object** | Source IP Address (`ip_address`) | Target Account (`username`) |
| **Aggregation Key** | `IP` count of total `FAILED` status logs | `Username` set of unique `password_attempted` values |
| **Threat Vector** | Network scanner / Automated IP attack | Targeted dictionary attack / Password spraying |
| **Primary Metric** | Failed attempts count per IP ($\ge 3$) | Distinct failed passwords per User ($\ge 3$) |
| **Mitigation Action** | Block IP address at Firewall / WAF | Force target user password reset & mandate MFA |

---

## 4. Development Challenges & Resolution Strategies

1. **Short Passwords Penalty**: Enforced max score cap of 45 for passwords $< 8$ chars.
2. **CSPRNG Guarantee**: Guaranteed 1 character per selected pool before shuffling.
3. **Distinct Set Cardinality**: Utilized `set()` data structures to isolate dictionary attacks from repeated mistypes.

---

## 5. Code Verification & Test Results

All modules have been thoroughly validated using `unittest`:
```bash
python -m unittest discover -s tests
```
**Test Results**: `13 tests run — PASS (OK)`
