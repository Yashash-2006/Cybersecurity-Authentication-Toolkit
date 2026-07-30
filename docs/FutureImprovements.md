# Future Improvements & Expansion Roadmap

This document outlines the strategic technical enhancements planned for future major releases of the Cybersecurity Authentication Toolkit.

---

## 1. Cryptographic Password Hashing (bcrypt / Argon2id)

- **Current State**: Uses plaintext string comparisons for simulation purposes.
- **Future Upgrade**: Implement industry-standard password hashing using `bcrypt` or `Argon2id` with cryptographically random salts.
- **Benefits**: Protects credentials at rest against database leaks and rainbow table attacks.

```python
import bcrypt

# Example future implementation
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12))
is_valid = bcrypt.checkpw(entered_password.encode('utf-8'), hashed)
```

---

## 2. Relational & NoSQL Database Persistence

- **Current State**: Processes in-memory lists and static JSON/CSV log files.
- **Future Upgrade**: Integrate SQLite / PostgreSQL for relational transactional logging and MongoDB for unstructured high-volume SIEM log storage.

---

## 3. Adaptive Multi-Factor Authentication (MFA & TOTP)

- **Current State**: Evaluates single-factor username/password logins.
- **Future Upgrade**: Introduce Time-based One-Time Passwords (TOTP via Google Authenticator / Authy) and step-up MFA triggered dynamically whenever risk scores escalate.

---

## 4. Time-Sliding Rate Limiting & SIEM Integration

- **Current State**: Static cumulative count across all historical log entries.
- **Future Upgrade**: Implement sliding-window rate limiters (e.g., 3 failed attempts in 60 seconds) backed by Redis key expiration, with automated Syslog / CEF emission to Enterprise SIEMs (Splunk, Elastic SIEM).

---

## 5. Web & REST API Interface (FastAPI / CustomTkinter GUI)

- **Current State**: Rich Terminal Command Line Interface.
- **Future Upgrade**: Build a responsive web dashboard using FastAPI + React, and a standalone Desktop app using CustomTkinter.
