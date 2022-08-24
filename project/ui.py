from student import Student


class Ui:
    def __init__(self, manager):
        self.manager = manager
    
    def main_menu(self):
        print()
        print("=" * 60)
        print()
        
        print(">>> MAIN MENU <<<")
        print("1. Add Student")
        print("2. Show List")
        print("3. Exit")
        print()
        
        user_choice = input("Please choose a number: ")
        
        print()
        
        if user_choice == "1":
            self.add_student()
        elif user_choice == "2":
            print(self.manager.get_students_list())
        elif user_choice == "3":
            return -1
        else:
            print("Please enter a valid number.")
    
    def add_student(self):
        print()
        print("-" * 30)
        print()
        
        print(">>> ADD USER <<<")
        
        first_name = input("first name: ")
        last_name = input("last name: ")
        student_id = input("student id: ")
        major = input("major: ")
        average = float(input("average: "))
        
        student = Student(first_name, last_name, student_id, major, average)
        self.manager.students.append(student)
        
        print()
        print("Student has been added successfully.")
