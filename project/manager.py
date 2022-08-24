from student import Student


class Manager:
    def __init__(self):
        self.students = []
        self.load_data()
    
    def get_students_list(self):
        result = ""
        
        for student in self.students:
            result += f"[{student.student_id}] {student.first_name} {student.last_name} " \
                      f"(major: {student.major}, average: {student.average})\n"
        
        return result
    
    def load_data(self):
        file = open("students.txt", "r")
        lines = file.readlines()
        
        self.students = []
        for line in lines:
            [first_name, last_name, student_id, major, average] = line.split(";")
            self.students.append(Student(first_name, last_name, student_id, major, float(average)))
    
    def save_data(self):
        file = open("students.txt", "w")
        
        for student in self.students:
            file.write(str(student) + "\n")
