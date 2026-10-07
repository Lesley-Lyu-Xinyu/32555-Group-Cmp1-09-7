import pickle
import os

class Database:
    def load(self):
        if os.path.exists("students.data"):
            with open("students.data", "rb") as file:
                students = pickle.load(file)
        else:
            students = []
            self.save(students)
        return students

    def save(self, students):
        with open("students.data", "wb") as file:
            pickle.dump(students, file)

    def clear(self):
        with open("students.data", "wb") as file:
            pickle.dump([], file)
