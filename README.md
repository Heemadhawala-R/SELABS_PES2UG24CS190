# SE LABS


## Student Details

| Field | Details |
|---|---|
| Name | Heemadhawala R |
| SRN | PES2UG24CS190 |
| Semester | 5 |
| Section | D |

---

## Lab Submissions

## Problem Statement #04 – Student Project Portfolio & Showcase App

This repository contains the Software Engineering Lab submissions for the **Student Project Portfolio & Showcase App**.

The system provides a centralized platform for student teams to showcase their projects, submit multimedia artifacts, receive evaluations from panel judges, participate in public voting, and publish the final leaderboard.


### LAB 1 – Requirements Engineering & UML Use-Case Modelling

This lab includes:

- Functional Requirements
- Non-Functional Requirements
- Acceptance Criteria and Rationales
- UML Use-Case Diagram
- Actors and Use Cases
- `<<include>>` and `<<extend>>` relationships
- Use-Case Flow Specification

**Folder:** `LAB1/`

---

### LAB 2 – Agile Backlog Creation & Sprint Simulation in Jira

This lab includes:

- Jira Product Backlog
- Epics and User Stories
- Story Point Estimation
- Backlog Prioritization
- Sprint Planning
- Active Sprint Board
- Burndown Chart
- Sprint Simulation
- Reflection Questions
- Conclusion

**Folder:** `LAB2/`

---

### LAB 3 – Component Modelling & Architectural Pattern Selection

This lab includes:

- Architectural Pattern Evaluation
- Selection of Layered Architecture
- UML Component Diagram
- Component Interactions
- Data Flow
- Provided and Required Interfaces
- Architectural Justification
- Security Advantage
- Performance Benefit

**Folder:** `LAB3/`

---

### LAB 4 – Target Shooting Game

**Project Repository:** [04_target_shooting](https://github.com/Heemadhawala-R/04_target_shooting)

This lab involves developing and improving a Python-based target shooting game using Pygame.

The project includes:

- Game engine and rendering modules
- Target interaction and hit detection
- Target shooting gameplay
- Python source code and dependencies
- Before-and-after demonstration recordings

**Folder:** `LAB4/04_target_shooting/`

**Technologies:** Python, Pygame, Git, and GitHub.

---

### LAB 5 – Static Code Analysis: Fitness Club Class Booking Ledger

**Project Repository:** [L5_04_fitness_booking](https://github.com/Heemadhawala-R/L5_04_fitness_booking)

This lab focuses on improving the quality, security, style, and maintainability of a Python-based Fitness Club Class Booking Ledger.

The program manages fitness class bookings for activities such as Yoga, HIIT, and Spin. It supports member bookings, cancellations, capacity management, guest bookings, displaying class rosters, and exporting booking information to a JSON file.

#### Tools Used

- **Pylint:** Identifies potential programming issues and evaluates code quality.
- **Bandit:** Detects potential security vulnerabilities.
- **Flake8:** Checks Python formatting and compliance with style guidelines.

#### Issues Identified and Fixed

- Potential command-injection vulnerability caused by shell command execution.
- Mutable default arguments.
- Incorrect class-capacity checks.
- Bare exception handling.
- Missing file encoding and context managers.
- Invalid class capacities and guest counts.
- Missing docstrings and inconsistent naming conventions.
- Formatting and dictionary iteration improvements.

#### Static Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 6.60/10 | 10.00/10 |
| Bandit | 1 high-severity finding | No issues identified |
| Flake8 | 10 reported violations | No violations reported |

*Results are based on the reported analysis runs and should correspond to the reports in the project repository.*

#### Important Project Files

- `gym_system.py` — Corrected Python application.
- `issues.md` — Documented issues and fixes.
- `pylint_report.txt` and `pylint_report_after.txt`
- `bandit_report.txt` and `bandit_report_after.txt`
- `flake8_report.txt` and `flake8_report_after.txt`
- `reflection.md` — Lab reflection answers.

**Folder:** `LAB5/`

**Technologies:** Python, Pylint, Bandit, Flake8, Git, and GitHub.

---

## Repository Structure

```text
SELABS/
│
├── LAB1/
│   └── Lab 1.pdf
│
├── LAB2/
│   └── Lab 2.pdf
│
├── LAB3/
│   ├── Lab 3 Component Diagram
│   ├── Lab 3 Component Diagram PDF
│   └── Lab 3 Written Justification PDF
│
├── LAB4/
│   └── 04_target_shooting/
│       ├── Demo/
│       │   ├── target_shooting_before_changes.mov
│       │   └── final_target_shooting.mov
│       ├── target-shooting/
│       ├── README.md
│       └── .gitignore
│
├── LAB5/
│   └── Fitness Club Class Booking Ledger files
│
└── README.md
```

*The structure above is illustrative. Actual filenames and folder contents may differ.*

---

## Learning Outcomes

Through these laboratory exercises, I gained practical experience in requirements engineering, UML modelling, Agile project management, software architecture, Python application development, static code analysis, secure coding practices, and version control.

## Author

**Heemadhawala R**  
B.Tech – Computer Science and Engineering  
PES University
