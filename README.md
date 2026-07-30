# Cybersecurity Authentication Toolkit

```text
===================================================================
   ______ _____  ____ _____    _  _____   ____ ____ ______   __
  / ___/ / / / |/ / // / _ \  / |/ / _ \ / __// __//  _/ /  / /
 / /__/ /_/ /    / _  / // / /    / // // _/ _\ \  / // /__/ / 
 \___/\____/_/|_/_//_/\___/ /_/|_/\___//___//___//___/____/_/  
                                                               
                 SECURE AUTHENTICATION TOOLKIT
===================================================================
```

A Python-based cybersecurity toolkit simulating secure authentication mechanisms, password evaluation, CSPRNG password generation, and detection algorithms for brute-force and password-guessing attacks.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Workflow](#project-workflow)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Introduction

The **Cybersecurity Authentication Toolkit** is an educational and practical security framework built to demonstrate modern authentication protection and identity threat analysis. Designed for cybersecurity students and developers, it implements heuristic password evaluations, stateful login lockout limits, cryptographically secure password generation, and automated log analysis engines for IP brute-forcing and targeted account dictionary attacks.

---

## Features

- **Module 1: Password Strength Checker**: Calculates Shannon Entropy ($\text{bits}$), evaluates character set diversity, caps short passwords, flags leaked weak passwords, and outputs actionable feedback.
- **Module 2: Login Lockout Simulator**: Enforces a strict 3-attempt lockout policy on protected accounts, dynamically computing remaining attempts and rejecting locked access.
- **Module 3: Secure Password Generator**: Leverages Python's `secrets` module (CSPRNG) with guaranteed category inclusion (uppercase, lowercase, digits, special symbols).
- **Module 4: Brute-Force Attack Detection**: Analyzes authentication logs, aggregates failure counts per source IP address, and flags IPs with $\ge 3$ failed attempts.
- **Module 5: Password Guessing Detection**: Tracks unique failed password variations attempted per username, isolating targeted dictionary attacks from user typing errors.

---

## Technologies

- **Language**: Python 3.10+
- **Terminal UI**: `rich`, `colorama`
- **Security & Math**: `secrets` (CSPRNG), `math`, `re`, `collections`
- **Testing**: `unittest`
- **Data Ingestion**: JSON, CSV

---

## Folder Structure

```text
Cybersecurity-Authentication-Toolkit/
│
├── src/
│   ├── main.py                   # Main Interactive CLI Driver
│   ├── password_checker.py       # Module 1: Strength Checker
│   ├── login_lockout.py          # Module 2: Lockout Simulator
│   ├── password_generator.py     # Module 3: Secure Generator
│   ├── brute_force_detector.py   # Module 4: IP Brute Force Detector
│   ├── password_guess_detector.py# Module 5: Password Guess Detector
│   └── utils.py                  # Log Parsers & UI Utilities
│
├── sample_data/
│   ├── sample_login_logs.json    # JSON Authentication Logs
│   ├── login_attempts.csv        # CSV IP Attack Logs
│   └── password_attempts.csv     # CSV User Attack Logs
│
├── screenshots/
│   └── README.md                 # Screenshot Descriptions
│
├── docs/
│   ├── Project_Report.md         # Written Technical Report
│   ├── Architecture.md           # System Architecture & Diagrams
│   ├── DetectionLogic.md         # Mathematical & Algorithmic Logic
│   └── FutureImprovements.md     # Project Roadmap & Enhancements
│
├── tests/
│   ├── test_password_checker.py  # Module 1 Unit Tests
│   ├── test_login_lockout.py     # Module 2 Unit Tests
│   ├── test_generator.py        # Module 3 Unit Tests
│   └── test_detectors.py        # Module 4 & 5 Unit Tests
│
├── main.py                       # Top-Level Project Entry Point
├── generate_demo_outputs.py      # Screenshot Output Log Generator
├── README.md                     # Project Documentation
├── requirements.txt              # Dependency Manifest
├── LICENSE                       # MIT License
├── .gitignore                    # Python Git Ignore Rules
└── CHANGELOG.md                  # Release Version Log
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Cybersecurity-Authentication-Toolkit.git
   cd Cybersecurity-Authentication-Toolkit
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

### Interactive Terminal Interface
```bash
python main.py
```

### Automated Unit Test Suite
```bash
python -m unittest discover -s tests
```

### Generate Visual Demonstration Log
```bash
python generate_demo_outputs.py
```

---

## Project Workflow

```text
User Selects Option / Inputs Logs
              │
              ▼
    Interactive Main CLI Driver (src/main.py)
              │
              ▼
   Cybersecurity Security Engine
 ├── [Module 1] Heuristics + Shannon Entropy Score
 ├── [Module 2] Stateful Account Attempt Lockout Gate
 ├── [Module 3] CSPRNG Category Selection & Array Shuffle
 ├── [Module 4] Source IP Aggregation & Threshold Filter (>=3)
 └── [Module 5] Username Distinct Password Set Analysis (>=3)
              │
              ▼
   Rich Terminal Report & Incident Security Alert
```

---

## Future Improvements

- **bcrypt / Argon2id Hashing**: Secure hashed storage for credentials.
- **Database Backend**: SQLite & MongoDB SIEM log persistence.
- **Time-Sliding Rate Limiting**: Sliding window decay for login attempts.
- **Adaptive MFA**: Step-up TOTP verification upon risk detection.
- **Web Interface**: FastAPI REST endpoints and React Dashboard.

---

## Author

- **Yashash Chandra Yellampalli**
- **Course**: Python for Cybersecurity
- **Topic Tags**: `python` | `cybersecurity` | `authentication` | `password-security` | `brute-force` | `password-generator` | `login-system` | `security-tools`

---

## License

This project is licensed under the [MIT License](LICENSE).
