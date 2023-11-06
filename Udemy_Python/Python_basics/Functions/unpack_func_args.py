#multiple arguments can be passed in function or unpacked in function.

#in the function below we pass 3 seperate arguments in add. The * before args collects these in a tuple and then u can iterate the tuple and use it as required
def add(*args):
    total = 0
    for x in args:
        total = total +x
    print(total)


add(4,5,6)

#In this function, we just pass one argument while calling function but * before it unpacks the args into x and y assigns values
def mult(x,y):
    print(x)
    print(y)
    print(x*y)

list1 = [2,4]

mult(*list1)

def mult(*args):
    print(args)
    total = 1
    for arg in args:
        total = total*arg
    return total

def apply(*args, operator):
    if operator == "*":
        return mult(*args)
    elif(operator == "+"):
        return sum(args)
    else:
        return "Enter Valued operator"
    

print(apply(1,3,4,5, operator="*"))


#Unpacking keyword arguments

def dict_unpack(name,age):             #keyword arguments should be same as keyword in dicts
    print(name,age)

dict1 = {"name":"Bob","age":25}
#dict_unpack(name="Bob",age=25)                use **args in function parameters and these named arguments will be collected and passed as dictionary to function

dict_unpack(**dict1)

