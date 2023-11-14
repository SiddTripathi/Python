#Simpler than inheritance with a concept if B inherits class A, then B is A but not vice versa. Composition means A has many classes one of them is B. 
#Inheritance is of no use if u inherit but never use methods in parent class. So we have composition. So in compostion parent and child class are independent.
#example

class CarCompany:
    def __init__(self, *car):
        self.car = car
    def __str__(self):
        return f"Car company has {len(self.car)} car models"

class CarModel:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"Car name - {self.name}"



car1 = CarModel("Polo")
car2 = CarModel("Passat")

company = CarCompany(car1,car2)
print(company)
# company is passing two carmodel objects which will be stored in a tuple. In order to print car name, you need to traverse tuple and run print function on it.
print(*company.car)  #one method is to unpack the tuple and run print on it --> similar to line 26
print(car1,car2)

all_cars = [print(car) for car in company.car] #another method is that traverse the tuple and print each element.
