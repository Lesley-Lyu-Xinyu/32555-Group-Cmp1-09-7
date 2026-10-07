import random

class Subject:
    def __init__(self):
        self.id = str(random.randint(1, 999)).zfill(3)
        self.mark = random.randint(25, 100)

        if self.mark < 50:
            self.grade = "Z"
        elif self.mark < 65:
            self.grade = "P"
        elif self.mark < 75:
            self.grade = "C"
        elif self.mark < 85:
            self.grade = "D"
        else:
            self.grade = "HD"
