# Constructor and Destructor

class Student:

    # Constructor
    def __init__(self, name):
        self.name = name
        print("Constructor Called")

    def display(self):
        print("Student Name:", self.name)

    # Destructor
    def __del__(self):
        print("Destructor Called")

student = Student("Kapil")
student.display()

del student