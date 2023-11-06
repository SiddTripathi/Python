#Simple  Class implementation
class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def student_avg(self):
        return sum(self.grades)/len(self.grades)


student1 = Student("Bob",(100,100,60,80))
student2 = Student("Ryan",(80,90,100,50))


print(student1.student_avg())
print(student2.student_avg())


#self is just a normal parameter of method which is used to point to current instance of object and access the attributes of object. Like in above method accessing grades intitiated in init 
# mthod, or constructor

#Magic Methods
#__init__, __str__, __repr__

class Test:
    def __init__(self,name,city):
        self.name= name
        self.city=city
    #def __str__(self):
        #return f"Person {self.name}, lives in {self.city}"           #__str__ changes object print output. This will be now more presentable
    
    def __repr__(self):
        return f"<Person({self.name},{self.city})"                   #repr method is used in some places like debugger etc. Mostly its __str__ used

bob = Test("Bob","Auckland")

print(bob) # --> this will print a output which is not user friendly - <__main__.Test object at 0x000001C41F99F810>



#Test 

class Store:
    def __init__(self,name):
        self.name = name
        self.items = []
    def add_item(self, name, price):
        dict1 = {"name":name,"price":price}
        self.items.append(dict1)
        print(self.items[:])
    def stock_price(self):
        total = 0
        return sum([item['price'] for item in self.items])
    
        # Create a dictionary with keys name and price, and append that to self.items.

    
      


store1 = Store("Rayban")
store1.add_item("Pork",25)
store2 = Store("Raymes")
store2.add_item("Beef",45)
store2.add_item("Chips",34)
print(store2.stock_price())
store3 = Store("Rayvan")
store3.add_item("Chicken",66)