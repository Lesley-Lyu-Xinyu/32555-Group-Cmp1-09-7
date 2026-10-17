# CLIUniApp & GUIUniApp - Group 09 (Cmp1-09-7)

## Project
CLIUniApp is a command-line university enrolment system built in Python.
It is based on our design from Assessment 1 - Part 1.
It has four menus: University System, Student System, Subject Enrolment System and Admin System.
GUIUniApp is a separate window app. Registered students can log in and enrol in subjects.
All data is saved in the file `students.data`.

## Group Members and Contributions
| Member | Part | Files | Main work |
|---|---|---|---|
| Rira Seo | Database | `database.py` | Database class: checks if `students.data` exists and creates it, loads and saves students, clears all data, handles an empty or broken file |
| Xinyu Lyu | Student | `student.py`, `students.data` | Student class: id, name, email, password and subjects list; enrol (max 4 subjects), remove a subject, show subjects, average mark, change password |
| Ana Paula Moreira Catao | Subject | `subject.py` | Subject class: random 3-digit id (001-999), random mark (25-100), grade from the mark (Z, P, C, D, HD) |
| Akash Nagarkar | GUI | `gui.py` | GUIUniApp: login window, enrolment window (max 4 subjects), subject window (marks and grades), exception window (empty fields, wrong format, wrong login, more than 4 subjects) |
| All members | Menus and integration | `main.py` | Built together: University, Student, Subject Enrolment and Admin menus; joined all classes into one software and tested the full program |

## Files
| File | What it does |
|---|---|
| `main.py` | Starts the CLI app and runs all the menus |
| `student.py` | Student class |
| `subject.py` | Subject class |
| `database.py` | Reads and writes `students.data` |
| `gui.py` | GUIUniApp (login, enrolment, subject and exception windows) |
| `students.data` | Saved student data |

## Grading System
| Grade | Meaning | Mark |
|---|---|---|
| HD | High Distinction | 85-100 |
| D | Distinction | 75-84 |
| C | Credit | 65-74 |
| P | Pass | 50-64 |
| Z | Fail | below 50 |

A student passes if the average mark of all subjects is 50 or more.

## Requirements
- Python 3
- No extra libraries. The GUI uses tkinter, which comes with Python.

## How to Run
CLI app:
```
python main.py
```

GUI app:
```
python gui.py
```

Note: register a student in the CLI app first. The GUI has login only.

## Login Format
- Email must end with `@university.com` (example: `john.smith@university.com`)
- Password must start with a capital letter, have at least 5 letters, and end with 3 or more numbers (example: `Helloworld123`)