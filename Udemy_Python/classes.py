class Student:
    def __init__(self,name,*grade):
        self.name = name
        self.grade = grade
    
    def average(self):
        avg = sum(self.grade)/len(self.grade)
        return avg
    def __str__(self):
        return f"This is <{self.name},{self.grade} object"


student =  Student('Sid',100,80,90,20)
student2 = Student('Nam',90,100,80,10)

print(student.name)
print(student.grade)
print(student)
print(student2.name)
print(student2.grade)
print(student.average())
print(student2.average())