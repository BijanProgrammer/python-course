class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        return f"first_name = {self.first_name}\n" \
               f"last_name = {self.last_name}\n" \
               f"age = {self.age}\n"


class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.major = major
    
    def __str__(self):
        return super().__str__() + f"student_id = {self.student_id}\n" \
                                   f"major = {self.major}\n"


bijan = Student('Bijan', 'Eisapour', 21, '972023026', 'CE')
print(bijan)
