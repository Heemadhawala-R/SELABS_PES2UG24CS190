# Lab 5: Static Code Analysis — Fitness Club Class Booking Ledger

**Python File:** `gym_system.py`

## 1. About the Program

The Fitness Club Class Booking Ledger is a Python program that manages bookings for fitness classes such as Yoga, HIIT, and Spin. It supports member bookings, cancellations, class capacity management, guest bookings, displaying class rosters, and exporting booking information to a JSON file.

The original program contained several code quality, logic, security, and style issues. This lab uses Pylint, Bandit, and Flake8 to identify and fix these issues.

## 2. Objective

To improve Python code quality, security, style, and maintainability using static code analysis tools.

## 3. Tools Used

- **Pylint:** Identifies potential programming issues and code quality problems.
- **Bandit:** Detects potential security vulnerabilities in Python code.
- **Flake8:** Checks Python formatting and compliance with style guidelines.

## 4. Procedure

1. Inspected `gym_system.py` and ran the original program.
2. Installed Pylint, Bandit, and Flake8 in the Python virtual environment.
3. Ran all three tools on the original code and saved the reports.
4. Examined the reports and documented the issues.
5. Fixed the identified problems in `gym_system.py`.
6. Reran the tools to verify the improvements.

## 5. Issues Identified and Fixed

The following table documents the issues found in the original code, their types, original line numbers, descriptions, and fix approaches.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution | Security — High | 36 | `os.system()` executes a constructed shell command, creating a potential command-injection vulnerability. | Replaced `os.system()` with safer file operations using `pathlib`. |
| Mutable default argument | Bug | 8 | `attendance_log=[]` shares a default list across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Incorrect capacity check | Logic bug | 12 | Using `>` instead of `>=` allows an extra booking when the class reaches its capacity. | Changed the condition to `>=` to prevent overbooking. |
| Bare exception | Code quality | 21 | A bare `except` can catch unrelated exceptions and hide errors. | Replaced it with `except (KeyError, ValueError)`. |
| Missing file encoding | Code quality | 32 | The file was opened without explicitly specifying an encoding. | Added `encoding="utf-8"`. |
| File resource handling | Code quality | 32 | The file was opened without a context manager. | Used `with open(...)` for proper resource management. |
| Invalid class capacity | Input validation | 47 | Negative class capacities were accepted. | Added validation for non-negative integer capacities. |
| Invalid guest count | Input validation | 28 | Invalid guest counts could cause unexpected behavior. | Added validation for non-negative integer counts. |
| Missing docstrings | Maintainability | Multiple | The module and functions lacked documentation. | Added module and function docstrings. |
| Naming convention | Style | 27 | `addMembers` did not follow Python's snake_case naming convention. | Renamed it to `add_members`. |
| Formatting and dictionary iteration | Style | 15, 39 | Old string formatting and dictionary key iteration reduced readability. | Used f-strings and `.items()` where appropriate. |

**Note:** Line numbers refer to the original code and may differ from the corrected version. Verify individual line numbers against the original reports before submission.

## 6. Static Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 6.60/10 | 10.00/10 |
| Bandit | 1 high-severity finding | No issues identified |
| Flake8 | 10 reported violations | No violations reported |

## 7. How to Run the Program

### Prerequisites

- Python installed on your system.
- A project virtual environment.

### Execution Steps

1. Open a terminal in the project directory.
2. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

3. Run the program:

   ```bash
   python gym_system.py
   ```

4. Enter the number of walk-in guests for HIIT when prompted, or press Enter to use the default value of `1`.

The program displays the class rosters and exports them to `gym_schedule.json`.

### Run Static Analysis

Use the following commands to generate the final reports:

```bash
pylint gym_system.py > pylint_report_after.txt 2>&1
bandit -r gym_system.py > bandit_report_after.txt 2>&1
flake8 gym_system.py > flake8_report_after.txt 2>&1
```

## 8. Project Files

- `gym_system.py` — Corrected Python application.
- `issues.md` — Detailed issue log and fixes.
- `pylint_report.txt` — Original Pylint report.
- `pylint_report_after.txt` — Final Pylint report.
- `bandit_report.txt` — Original Bandit report.
- `bandit_report_after.txt` — Final Bandit report.
- `flake8_report.txt` — Original Flake8 report.
- `flake8_report_after.txt` — Final Flake8 report.
- `reflection.md` — Reflection answers required by the lab.

## 9. Conclusion

This lab demonstrated how static code analysis can identify and help resolve programming, security, input validation, and style issues. After the improvements, the program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no violations.

These improvements make the Fitness Club Class Booking Ledger easier to read, maintain, and review for potential security issues.