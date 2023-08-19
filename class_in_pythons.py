class Student:
    def __init__(self):
        self.name = "Rolf"


student = Student()
print(student.name)



class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"<Person('{self.name}','{self.age}')>"
    # def __str__(self):
    #     return f"Person {self.name} is {self.age} old!"
    

person = Person("Tom",34)

print(person)

print(person.name)