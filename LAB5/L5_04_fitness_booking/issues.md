# Lab 5: Static Code Analysis — Issue Log

## Original Analysis Results
- Pylint: 6.60/10
- Bandit: 1 high-severity security finding
- Flake8: 10 reported violations

## Issues Identified and Fixed

| No. | Issue | Type | Description | Fix Applied |
|---|---|---|---|---|
| 1 | Mutable default argument | Bug risk | Default list could be shared across calls. | Used None and initialized a new list. |
| 2 | Capacity check | Logic bug | Extra booking was allowed when a class was full. | Changed > to >=. |
| 3 | Bare exception | Code quality | Caught unrelated exceptions. | Caught KeyError and ValueError. |
| 4 | Shell command execution | Security | Used os.system to construct a shell command. | Replaced it with pathlib operations. |
| 5 | File handling | Code quality | No explicit encoding or context manager. | Used with open(..., encoding="utf-8"). |
| 6 | Capacity validation | Input validation | Negative capacity was accepted. | Added non-negative integer validation. |
| 7 | Guest input | Input validation | Invalid input could cause an error. | Added input validation. |
| 8 | Missing docstrings | Maintainability | Module and functions lacked documentation. | Added docstrings. |
| 9 | Naming convention | Style | addMembers did not follow snake_case. | Renamed it to add_members. |
| 10 | Formatting | Style | Formatting and dictionary iteration needed improvement. | Used f-strings, .items(), and consistent spacing. |

## Final Analysis Results
- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No violations reported
