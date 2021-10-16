'''
Object Oriented Programming
'''

class Student:

    # Class variables
    school = 'Online School'
    number_of_students = 0

    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students =+ 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major.'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major at {self.school}'

    def greetings(self):
        return f'Hello, I am {self.first_name} {self.last_name}'

    # Decorator
    @classmethod
    def set_online_school(cls, new_school):
        # cls = class
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        # Return cls means returning an initialized instance
        return cls(first_name, last_name, major)


# Inheritance 
class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major, age):
        super().__init__(first_name, last_name, major)
        self.age = age

    # Overwrite existing method in student with custom one.
    def greetings(self):
        return f'Hello, I am {self.first_name} {self.last_name} and I am {str(self.age)} years old.'


student_1 = Student('Neo', 'Anderson', "Computer Science")
student_2 = CollegeStudent('John', 'Doe', 'Engineering', 21)

print(f'Number of students = {Student.number_of_students}')
print(student_1.fullname_major_school())
Student.set_online_school('Udemy')
print(student_2.greetings())
print(Student.fullname_major_school(student_2))

new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())
print(f'Number of students = {Student.number_of_students}')

