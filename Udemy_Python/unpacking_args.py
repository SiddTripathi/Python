#unpacking arguments

#program1 - multiple arguments in a function
def mul(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

#distributing dict key values as arguments into function args
def add(x,y):
    return x+y



#multiple arguments and specific args combiend

def apply(*args,operator):
    if operator == '*':
        return mul(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No Operator"






print(apply(1,3,5,operator='*'))





