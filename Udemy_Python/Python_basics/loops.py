# Loops are of two types - one which allow us to repeat code for certain number of times and one which allows to repeat code till a condition is True


number = 7

while (True):
    usr_inp = input("Like to Play a game (Y/N): ").lower()
    if usr_inp == 'n':
        print("Thanks For Playing")
        break
    usr_numb = int(input("Guess the number: "))
    if usr_inp == number:
        print("Correct Guess !!")
    elif abs(number - usr_numb) == 1:
        print("You were off by 1")
    else:
        print("Sorry Worng guess")


#For Loop

employee = ["Raj","Sweta","Pandit","Guddu","Babloo"]
a_employee = []
b_employee= []

for name in employee:
    A_or_B = input(f"Is {name} a good employee(Y/N): ").lower()
    if A_or_B == 'y':
        a_employee.append(name)
    elif A_or_B == 'n':
        b_employee.append(name)
    else:
        print("Wrong option ! Exiting")
        break


print(a_employee)
print(b_employee)