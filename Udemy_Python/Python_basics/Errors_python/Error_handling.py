#Now compared to earlier, in file no_error_handling, this raise keyword gives us more information than just printing statement
#We now get Divisor cannot be zero but also get, where the error is occuring such as line number etc.

def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return dividend/divisor


grades =[4,8]
print("Welcome to average grade")
average =  divide(sum(grades),len(grades))
print(f"Average of grades is {average}")


#making it more use friendly or clean, we use handling of error using try except (raise is like catch). The below program is more for users while above is more for
#developers to help them debug
print("*******************\nThis is Same program as above but with error handling\n************")


def divide1(dividend,divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return dividend/divisor


grade1 = []
print("This is grade program with error handling")
try:
    average = divide1(sum(grade1),len(grade1))
    print(f"The average grade is {average}")
    
except ZeroDivisionError as e:                 #  as e --> will create a variable which will print same error as in ZeroDivisionError message
    print("Looks like no grades to evaluate")
    print(e)

