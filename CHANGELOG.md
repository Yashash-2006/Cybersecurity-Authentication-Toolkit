# Changelog

All notable changes to the Cybersecurity Authentication Toolkit will be documented in this file.

## [1.0.0] - 2026-07-30

### Added
- **Module 1: Password Strength Checker**: Implemented heuristic scoring, Shannon Entropy calculation, short-password scoring cap, and weak password list filtering.
- **Module 2: Login Lockout Simulator**: Added stateful attempt tracking, maximum 3-failed-login lockout enforcement, remaining attempt counter, and administrative unlock capabilities.
- **Module 3: Secure Password Generator**: Built CSPRNG generator using Python standard `secrets` module with guaranteed category inclusion (uppercase, lowercase, digits, special characters) and array shuffling.
- **Module 4: Brute-Force Attack Detector**: Added IP-based failed login aggregation, threshold filtering ($\ge 3$), risk severity rating (`MEDIUM` / `HIGH`), and security alert generation.
- **Module 5: Password Guessing Detector**: Implemented targeted username tracking with unique failed password set cardinality analysis ($\ge 3$ distinct passwords) to distinguish dictionary attacks from user mistypes.
- **UI Engine**: Integrated `rich` console interface for tables, styled panels, colored logs, and interactive prompts.
- **Data Parsers**: Added support for ingestion of JSON (`sample_data/sample_login_logs.json`) and CSV (`sample_data/login_attempts.csv`, `sample_data/password_attempts.csv`) log datasets.
- **Test Suite**: Added 13 comprehensive unit tests covering all 5 modules with 100% pass rate.
- **Documentation**: Created `docs/` folder containing `Project_Report.md`, `Architecture.md`, `DetectionLogic.md`, and `FutureImprovements.md`.
