from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, student_id, major, average):
        super().__init__(first_name, last_name)
        self.student_id = student_id
        self.major = major
        self.average = average
    
    def __str__(self):
        return super().__str__() + f";{self.student_id};{self.major};{self.average}"
