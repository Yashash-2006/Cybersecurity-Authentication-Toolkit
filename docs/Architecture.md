# System Architecture Documentation

## Overview

The **Cybersecurity Authentication Toolkit** follows a modular, layer-separated architecture designed for security analysis, extensible feature addition, and ease of demonstration.

---

## Architectural Diagram

```text
+-----------------------------------------------------------------------+
|                           User Interface                              |
|         Command Line Interface (src/main.py with Rich UI)             |
+------------------------------------+----------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------+
|                           Core Modules (src/)                         |
|                                                                       |
|  +--------------------------+     +-------------------------------+   |
|  | Module 1:                |     | Module 2:                     |   |
|  | password_checker.py      |     | login_lockout.py              |   |
|  +--------------------------+     +-------------------------------+   |
|                                                                       |
|  +--------------------------+     +-------------------------------+   |
|  | Module 3:                |     | Module 4:                     |   |
|  | password_generator.py    |     | brute_force_detector.py       |   |
|  +--------------------------+     +-------------------------------+   |
|                                                                       |
|  +--------------------------+     +-------------------------------+   |
|  | Module 5:                |     | Utilities & Parsers:          |   |
|  | password_guess_detector  |     | utils.py                      |   |
|  +--------------------------+     +-------------------------------+   |
+------------------------------------+----------------------------------+
                                     |
                                     v
+-----------------------------------------------------------------------+
|                           Data Layer                                  |
|  sample_data/login_attempts.csv     sample_data/sample_login_logs.json|
|  sample_data/password_attempts.csv                                    |
+-----------------------------------------------------------------------+
```

---

## Data Flow Pipeline

```text
User Input / Log File Ingestion
              │
              ▼
   Dataset Parsing & Normalisation (src/utils.py)
              │
              ▼
     Security Analysis Engine
  ├── Module 1: Heuristic + Entropy Calculations
  ├── Module 2: State Tracking & Lockout Policy Enforcement
  ├── Module 3: CSPRNG Selection & Array Shuffle
  ├── Module 4: IP-based Failure Aggregation & Threshold Filtering
  └── Module 5: Username Distinct Password Cardinality Analysis
              │
              ▼
    Rich Terminal Visualisation & Security Alert Reports
```
