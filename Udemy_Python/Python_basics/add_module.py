def add(num1,num2):
    return num1+num2


def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return dividend/divisor