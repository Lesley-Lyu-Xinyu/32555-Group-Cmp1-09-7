from subject import Subject

class Student:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []

    def enroll(self):
        if len(self.subjects) >= 4:
            print("\t\tStudents are allowed to enrol in 4 subjects only")
        else:
            new_subject = Subject()
            while self.has_subject(new_subject.id):
                new_subject = Subject()
            print("\t\tEnrolling in Subject-" + new_subject.id)
            self.subjects.append(new_subject)
            print("\t\tYou are now enrolled in", len(self.subjects), "out of 4 subjects")

    def has_subject(self, subject_id):
        for s in self.subjects:
            if s.id == subject_id:
                return True
        return False

    def remove(self, subject_id):
        found = None
        for s in self.subjects:
            if s.id == subject_id:
                found = s

        if found:
            print("\t\tDroping Subject-" + found.id)
            self.subjects.remove(found)
            print("\t\tYou are now enrolled in", len(self.subjects), "out of 4 subjects")
        else:
            print("\t\tSubject does not exist")

    def show(self):
        print("\t\tShowing", len(self.subjects), "subjects")
        for s in self.subjects:
            print("\t\t[ Subject::" + s.id + " -- mark = " + str(s.mark) + " -- grade = " + "{:>3}".format(s.grade) + " ]")

    def get_average(self):
        if len(self.subjects) == 0:
            return 0
        total = 0
        for subject in self.subjects:
            total = total + subject.mark
        average = total / len(self.subjects)
        return average

    def change_password(self, new_password):
        self.password = new_password
