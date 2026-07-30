# Module Demonstration Screenshots

This folder contains screenshot guides and instructions for demonstrating execution of each module for submission.

## Expected Screenshot Files

1. **`module1.png`**: Password Strength Checker Output
   - Run: `python main.py` $\rightarrow$ Option 1
   - Evaluates password length, Shannon entropy, character categories, and recommendations.
   - <img width="930" height="883" alt="Screenshot 2026-07-30 155753" src="https://github.com/user-attachments/assets/5dfb7430-669c-446c-8bf9-d523f69d1d26" />

2. **`module2.png`**: Login Lockout Simulator Output
   - Run: `python main.py` $\rightarrow$ Option 2
   - Shows remaining attempts (`2`, `1`, `0`), account lockout on 3rd failure, and lockout enforcement on subsequent attempts.
   - <img width="1057" height="846" alt="Screenshot 2026-07-30 155814" src="https://github.com/user-attachments/assets/60eabd09-97ed-4d16-937d-c0605b287e1b" />


3. **`module3.png`**: Secure Password Generator Output
   - Run: `python main.py` $\rightarrow$ Option 3
   - Demonstrates CSPRNG generated passwords and automatic strength rating.
   - <img width="935" height="731" alt="Screenshot 2026-07-30 155829" src="https://github.com/user-attachments/assets/a0b1118f-ea05-4000-9288-0d5f13398035" />


4. **`module4.png`**: Brute Force Attack Detection Output
   - Run: `python main.py` $\rightarrow$ Option 4
   - Shows table of flagged IP addresses ($\ge 3$ failed attempts) with risk levels and targeted accounts.
   - <img width="941" height="691" alt="Screenshot 2026-07-30 155845" src="https://github.com/user-attachments/assets/d960289a-b60d-4b59-8c99-8ffb4577f130" />


5. **`module5.png`**: Password Guessing Detection Output
   - Run: `python main.py` $\rightarrow$ Option 5
   - Shows table of targeted user accounts ($\ge 3$ distinct passwords tried), distinct password count, sample passwords, and source IPs.
   - <img width="992" height="731" alt="Screenshot 2026-07-30 155855" src="https://github.com/user-attachments/assets/3693194e-77ce-4024-b8d5-e47c884a7402" />



---

### Automated Log Generation for Screenshots
You can run the demonstration script to display formatted output logs for all 5 modules simultaneously:
```bash
python generate_demo_outputs.py
```
