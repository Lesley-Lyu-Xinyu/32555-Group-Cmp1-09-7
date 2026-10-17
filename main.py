import random
import re
from database import Database
from student import Student

EMAIL_PATTERN = r"^[\w.-]+@university\.com$"
PASSWORD_PATTERN = r"^[A-Z][A-Za-z]{4,}\d{3,}$"

def is_valid_email(email):
    return re.match(EMAIL_PATTERN, email) is not None

def is_valid_password(password):
    return re.match(PASSWORD_PATTERN, password) is not None

def find_student_by_email(students, email):
    for s in students:
        if s.email == email:
            return s
    return None

def id_exists(students, student_id):
    for s in students:
        if s.id == student_id:
            return True
    return False

def course_menu(student, db, students):
    while True:
        choice = input("\t\tStudent Course Menu (c/e/r/s/x): ")
        choice = choice.strip().lower()

        if choice == "c":
            print("\t\tUpdating Password")
            new_password = input("\t\tNew Password: ")
            while True:
                confirm_password = input("\t\tConfirm Password: ")
                if new_password == confirm_password:
                    student.change_password(new_password)
                    db.save(students)
                    break
                print("\t\tPassword does not match - try again")
        elif choice == "e":
            student.enroll()
            db.save(students)
        elif choice == "r":
            subject_id = input("\t\tRemove Subject by ID: ")
            student.remove(subject_id)
            db.save(students)
        elif choice == "s":
            student.show()
        elif choice == "x":
            return
        else:
            print("\t\tInvalid option")

def student_menu(db):
    students = db.load()

    while True:
        choice = input("\tStudent System (l/r/x): ")
        choice = choice.strip().lower()

        if choice == "l":
            print("\tStudent Sign In")

            while True:
                email = input("\tEmail: ")
                password = input("\tPassword: ")
                if is_valid_email(email) and is_valid_password(password):
                    print("\temail and password formats acceptable")
                    break
                print("\tIncorrect email or password format")

            student =find_student_by_email(students, email)

            if student is not None and student.password == password:
                course_menu(student, db, students)
            else:
                print("\tStudent does not exist")
        elif choice == "r":
            print("\tStudent Sign Up")

            while True:
                email = input("\tEmail: ")
                password = input("\tPassword: ")
                if is_valid_email(email) and is_valid_password(password):
                    print("\temail and password formats acceptable")
                    break
                print("\tIncorrect email or password format")

            existing =find_student_by_email(students, email)

            if existing:
                print("\tStudent", existing.name, "already exists")
            else:
                name = input("\tName: ")
                student_id = str(random.randint(1, 999999)).zfill(6)
                while id_exists(students, student_id):
                    student_id = str(random.randint(1, 999999)).zfill(6)
                new_student = Student(student_id, name, email, password)
                students.append(new_student)
                db.save(students)
                print("\tEnrolling Student", name)
        elif choice == "x":
            return
        else:
            print("\tInvalid option")

def average_grade(average):
    if average < 50:
        return "Z"
    elif average < 65:
        return "P"
    elif average < 75:
        return "C"
    elif average < 85:
        return "D"
    else:
        return "HD"

def format_student(s):
    average = s.get_average()
    grade = average_grade(average)
    return s.name + " :: " + s.id + " --> GRADE:  " + grade + " - MARK: " + "{:.2f}".format(average)

def admin_menu(db):
    while True:
        choice = input("\tAdmin System (c/g/p/r/s/x): ")
        choice = choice.strip().lower()

        if choice == "s":
            students = db.load()
            print("\tStudent List")
            if len(students) == 0:
                print("\t\t< Nothing to Display >")
            else:
                for s in students:
                    print("\t" + s.name + " :: " + s.id + " --> Email: " + s.email)
        elif choice == "g":
            students = db.load()
            print("\tGrade Grouping")
            if len(students) == 0:
                print("\t\t< Nothing to Display >")
            else:
                for grade in ["Z", "P", "C", "D", "HD"]:
                    group = []
                    for s in students:
                        if average_grade(s.get_average()) == grade:
                            group.append(format_student(s))
                    if len(group) > 0:
                        print("\t" + grade + "  --> [" + ", ".join(group) + "]")
        elif choice == "p":
            students = db.load()
            print("\tPASS/FAIL Partition")
            fail = []
            passed = []
            for s in students:
                if s.get_average() >= 50:
                    passed.append(format_student(s))
                else:
                    fail.append(format_student(s))
            print("\tFAIL --> [" + ", ".join(fail) + "]")
            print("\tPASS --> [" + ", ".join(passed) + "]")
        elif choice == "r":
            students = db.load()
            remove_id = input("\tRemove by ID: ")
            found = None
            for s in students:
                if s.id == remove_id:
                    found = s
            if found:
                students.remove(found)
                db.save(students)
                print("\tRemoving Student " + remove_id + " Account")
            else:
                print("\tStudent " + remove_id + " does not exist")
        elif choice == "c":
            print("\tClearing students database")
            confirm = input("\tAre you sure you want to clear the database (Y)ES/(N)O: ")
            if confirm.strip().upper() == "Y":
                db.clear()
                print("\tStudents data cleared")
        elif choice == "x":
            return
        else:
            print("\tInvalid option")

def main():
    db = Database()

    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ")
        choice = choice.strip().upper()

        if choice == "A":
            admin_menu(db)
        elif choice == "S":
            student_menu(db)
        elif choice == "X":
            print("Thank You")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
