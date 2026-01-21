class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        total = 0
        for student in self.students:
            total += student.score
        return total / len(self.students)


# --- Test ---
gradebook = Gradebook()

s1 = Student("Ali", 80)
s2 = Student("John", 70)
s3 = Student("Mary", 90)

gradebook.add_student(s1)
gradebook.add_student(s2)
gradebook.add_student(s3)

print("Class average:", gradebook.get_average())
# Expected: 80.0
