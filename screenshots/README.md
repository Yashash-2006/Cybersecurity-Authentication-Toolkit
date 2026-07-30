# Module Demonstration Screenshots

This folder contains screenshot guides and instructions for demonstrating execution of each module for submission.

## Expected Screenshot Files

1. **`module1.png`**: Password Strength Checker Output
   - Run: `python main.py` $\rightarrow$ Option 1
   - Evaluates password length, Shannon entropy, character categories, and recommendations.

2. **`module2.png`**: Login Lockout Simulator Output
   - Run: `python main.py` $\rightarrow$ Option 2
   - Shows remaining attempts (`2`, `1`, `0`), account lockout on 3rd failure, and lockout enforcement on subsequent attempts.

3. **`module3.png`**: Secure Password Generator Output
   - Run: `python main.py` $\rightarrow$ Option 3
   - Demonstrates CSPRNG generated passwords and automatic strength rating.

4. **`module4.png`**: Brute Force Attack Detection Output
   - Run: `python main.py` $\rightarrow$ Option 4
   - Shows table of flagged IP addresses ($\ge 3$ failed attempts) with risk levels and targeted accounts.

5. **`module5.png`**: Password Guessing Detection Output
   - Run: `python main.py` $\rightarrow$ Option 5
   - Shows table of targeted user accounts ($\ge 3$ distinct passwords tried), distinct password count, sample passwords, and source IPs.

---

### Automated Log Generation for Screenshots
You can run the demonstration script to display formatted output logs for all 5 modules simultaneously:
```bash
python generate_demo_outputs.py
```
