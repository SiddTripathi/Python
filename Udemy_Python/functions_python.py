#unpacking arguments


def mul(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(mul(1,3,5))
        

