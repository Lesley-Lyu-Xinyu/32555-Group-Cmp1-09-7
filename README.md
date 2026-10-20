# CLIUniApp & GUIUniApp - Group 09 (Cmp1-09-7)

## Project

CLIUniApp is a command-line university enrolment system built in Python. It is based on our design from Assessment 1 - Part 1. It has four menus: University System, Student System, Subject Enrolment System and Admin System. GUIUniApp is a separate window app. Registered students can log in and enrol in subjects. All data is saved in the file students.data.

## Group Members and Contributions

| Member | Part | Files | Main work |
|---|---|---|---|
| Rira Seo | Database and data handling | database.py, main.py (data handling and fixes), students.data | Database class: checks if students.data exists and creates it, loads and saves students, clears all data, handles an empty, broken or unreadable file. Added methods to find a student by email, check if a student ID already exists, and remove a student by ID. In main.py: connected all menus to the Database (loads data when a menu opens and saves after every change: register, enrol, remove subject, change password, remove student, clear database). Fixed main.py to match the sample I/O: password regex (Hello123 is rejected), password format check when changing password, and HD grade alignment in the admin output. Prepares the final students.data. |
| Xinyu Lyu | Student | student.py | Student class: id, name, email, password and subjects list; enrol (max 4 subjects), remove a subject, show subjects, average mark, change password |
| Ana Paula Moreira Catao | Subject | subject.py | Subject class: random 3-digit id (001-999), random mark (25-100), grade from the mark (Z, P, C, D, HD) |
| Akash Nagarkar | GUI | gui.py | GUIUniApp: login window, enrolment window (max 4 subjects), subject window (marks and grades), exception window (empty fields, wrong format, wrong login, more than 4 subjects) |
| All members | Menus and integration | main.py | Built together: University, Student, Subject Enrolment and Admin menus; joined all classes into one software and tested the full program |

Note: The first version of main.py (all four menus) was written together by all members in group sessions, with equal contribution. It was committed from one account, so GitHub shows only one author for that commit. Later changes to main.py were committed by the member who made them.

## Files

| File | What it does |
|---|---|
| main.py | Starts the CLI app and runs all the menus |
| student.py | Student class |
| subject.py | Subject class |
| database.py | Reads and writes students.data |
| gui.py | GUIUniApp (login, enrolment, subject and exception windows) |
| students.data | Saved student data. Created automatically by the Database class when the program first runs. |

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

    python main.py

GUI app:

    python gui.py

On macOS, use `python3` instead of `python` if needed.

Note: register a student in the CLI app first. The GUI has login only.

## Login Format

- Email must end with @university.com (example: john.smith@university.com)
- Password must start with a capital letter, followed by at least 5 more letters, and end with 3 or more numbers (example: Helloworld123). Hello123 is not valid.

## Showcase Demo Plan

We follow the order of the sample I/O. Each person continues with the student created by the person before them, so the demo runs as one connected flow.

| Order | Member | Demo | Marking criteria |
|---|---|---|---|
| 1 | Rira Seo | Menu navigation; register and login with regex check (e.g. Hello123 is rejected, as in the sample I/O); change password with format check; restart the program and log in again to show the data is saved in students.data | a. University System, b. Student System, c. Change password and Read/Write to file |
| 2 | Xinyu Lyu | Enrol in subjects (max 4, the 5th is rejected); show subjects; remove a subject; explain that the average mark is re-calculated with get_average() every time a subject is enrolled | c. Subject Enrolment System |
| 3 | Akash Nagarkar | Whole GUI: login window, enrolment window, subject window and exception windows (empty fields, wrong format, wrong login, more than 4 subjects) | e. GUIUniApp |
| 4 | Ana Paula Moreira Catao | Whole Admin system: show students, group by grade, PASS/FAIL, remove a student, clear the database. In g and p, explain that MARK is the average from Xinyu's get_average() and the grade comes from the Subject class | d. Admin System |

Why this order:

- Admin clear (c) deletes all students, so the Admin demo goes last.
- The GUI logs in with a student registered in the CLI, so the GUI demo comes before Admin.
- The MARK shown in Admin g and p should match the average of the marks Xinyu shows, which proves the average is calculated and saved correctly.

After each demo, each member briefly walks through their own code.
