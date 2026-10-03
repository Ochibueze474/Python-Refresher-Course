# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Jkagency", 22)
student2 = Student("Agbawo", 23)
student3 = Student("Emmanuel", 24)
student4 = Student("Victor", 25)

print()
print(f"The graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print()