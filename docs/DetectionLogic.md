# Detection Logic & Algorithmic Breakdown

This document details the exact mathematical formulas, regular expressions, and detection algorithms implemented across the toolkit.

---

## 1. Password Strength Scoring Logic (Module 1)

### Shannon Entropy Formula
$$E = L \times \log_2(N)$$

Where:
- $L$ = Length of password.
- $N$ = Character pool size:
  - Lowercase letters ($a-z$): $26$
  - Uppercase letters ($A-Z$): $26$
  - Numeric digits ($0-9$): $10$
  - Special symbols ($!@\#\dots$): $32$

### Scoring & Penalties
1. **Length Points**: $+3$ pts per char ($L < 8$), $+25$ pts ($8 \le L < 12$), $+35$ pts ($12 \le L < 16$), $+40$ pts ($L \ge 16$).
2. **Diversity Points**: $+10$ pts per enabled category (max $40$).
3. **Entropy Bonus**: $+20$ pts ($E \ge 60$), $+10$ pts ($E \ge 40$), $+5$ pts ($E \ge 25$).
4. **Penalties**:
   - Sequential repetition penalty: $-15$ pts for `(.)\1{2,}`.
   - Keyboard sequence penalty: $-10$ pts for `(012|123|234|abc|qwerty)`.
   - **Short Password Penalty Cap**: Passwords under 8 characters are strictly capped at $\le 45/100$.

---

## 2. Login Lockout Simulator Logic (Module 2)

```text
Initialize: failed_attempts = 0, is_locked = False, max_attempts = 3

On Login Attempt (user, password):
  IF is_locked == True THEN:
     RETURN "ACCOUNT LOCKED - ACCESS DENIED"
  
  IF user == target_user AND password == target_password THEN:
     failed_attempts = 0
     RETURN "SUCCESS"
  ELSE:
     failed_attempts += 1
     IF failed_attempts >= max_attempts THEN:
        is_locked = True
        RETURN "SECURITY ALERT: ACCOUNT LOCKED"
     ELSE:
        remaining = max_attempts - failed_attempts
        RETURN "FAILED - REMAINING: remaining"
```

---

## 3. Brute Force Detection Algorithm (Module 4)

```text
Input: Authentication Log Records (List of Dicts)
Threshold: 3 failed attempts per IP

Algorithm:
1. Initialize ip_counts = HashMap<IP, Int>()
2. FOR EACH log IN logs DO:
      IF log.status == "FAILED" THEN:
         ip_counts[log.ip_address] += 1
3. Flagged_IPs = { IP | ip_counts[IP] >= Threshold }
4. Generate High-Severity Security Alert for Flagged IPs
```

---

## 4. Targeted Password Guessing Detection Logic (Module 5)

```text
Input: Authentication Log Records (List of Dicts)
Threshold: 3 distinct failed passwords per Username

Algorithm:
1. Initialize user_passwords = HashMap<Username, Set<String>>()
2. FOR EACH log IN logs DO:
      IF log.status == "FAILED" THEN:
         user_passwords[log.username].add(log.password_attempted)
3. Flagged_Users = { User | Cardinality(user_passwords[User]) >= Threshold }
4. Generate Incident Alert (Distinguishes dictionary attack vs mistyped logins)
```
