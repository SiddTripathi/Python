#Guess Number

numbr = 7

while True:
    user_input = input("Would you like to play the game (y/n)")
    if user_input in ("n","N"):
        print("Thanks for playing")
        break
    user_number = int(input("Guess number - "))
    if user_number == numbr:
        print("Correct Guess")
    elif abs(numbr - user_number) == 1:
        print("You missed by 1")
    else:
        print("Incorrect Guess")


#Calculate average

grades = [35,50,34,27,67]
total = 0
amount  =len(grades)

for grade in grades:
    total +=grade


average = total/amount
print("Average of all grades - ",average)