class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []
    
    def append_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        return f"{self.student_id} ({self.first_name} {self.last_name}): {self.calculate_average()}"


bijan = Student("972023026", "Bijan", "Eisapour")
bijan.append_grade(20)
bijan.append_grade(20)
bijan.append_grade(19)
bijan.append_grade(16)
bijan.append_grade(9)
bijan.append_grade(18.5)

reza = Student("972023099", "Reza", "Eisapour")
reza.append_grade(7)
reza.append_grade(8)
reza.append_grade(9.75)
reza.append_grade(0)
reza.append_grade(19.5)

print(bijan)
print(reza)
