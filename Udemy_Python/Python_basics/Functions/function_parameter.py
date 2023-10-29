#simple argumet function

def print_double(x):
    return x*2



print(f"Double of 2 is {print_double(2)}")

#addition
def add_nums(x,y):
    return x+y

x = int(input("Enter First number = "))
y = int(input("Enter Second number = "))


print(f"sum of {x} and {y} = {add_nums(x,y)}")

#keyword argument - you can assign value to particular argument. Remember postional arguments first keyword arguments later


def divide(dividend,divisor):
    if divisor!=0:
        return dividend/divisor
    else:
        return "Zero cannot divide"


print(divide(divisor=2,dividend=4)) #This is correct
#print(divide(2,dividend=4)) #This is incorrect as first postional argument is dividend and the keyword argument is also dividend. So one thing cannot have two values
print(divide(8,divisor=4)) #This is correct as we dont have keyword in first argument but as a positional argument 8 will be assigned to dividend
#print(divide(dividend=4,2)) #This is incorrect as python error postional argument cannot appear after keyword


#default values cannot be followed by normal parameters. Default values means that now that parameter is optional

def add(x,y=4):
    return x+y

print(add(4))  #this will give x value 4 and y its default value
print(add(4,6))  #this will override the default value 4 to 6