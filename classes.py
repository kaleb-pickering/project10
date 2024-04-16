class Professor:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def greet_students(self):
        print("Welcome to class!")



# Write your code below:
class ISMProfessor(Professor):
    # instance attribute inherited
    def __init__(self, name, age, course):
        super().__init__(name, age, course)
    
    # Define a greet_students() method
    def greet_students(self):
        print("Hi everyone! It's a great day to study ISM 480!")
        super().greet_students()