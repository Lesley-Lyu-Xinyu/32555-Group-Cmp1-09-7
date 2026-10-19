import pickle
import os

# students.data is always kept next to this file,
# so it works no matter which folder the program is run from
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.data")

class Database:
    def load(self):
        # create the file if it does not exist
        if not os.path.exists(FILE_PATH):
            self.save([])
            return []
        # if the file is empty or damaged, start with an empty list
        try:
            with open(FILE_PATH, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return []

    def save(self, students):
        with open(FILE_PATH, "wb") as file:
            pickle.dump(students, file)

    def clear(self):
        self.save([])
        
    def find_student_by_email(self, students, email):
        for s in students:
            if s.email == email:
                return s
        return None

    def id_exists(self, students, student_id):
        for s in students:
            if s.id == student_id:
                return True
        return False

    def remove_student_by_id(self, student_id):
        students = self.load()

        for s in students:
            if s.id == student_id:
                students.remove(s)
                self.save(students)
                return True

        return False