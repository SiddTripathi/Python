import random

def random_guess(usr_inp):
    comp_guess = random.randint(1,9)
    i = 1
    count=0
    while(i!=0):
        if(comp_guess<usr_inp):
            print("Your guess is too high ! Guess lower")
            
        elif(comp_guess>usr_inp):
            print("Your guess is too low ! Guess higher")
            
        else:
            print("Hurray ! You have guessed the number correctly")
        count+=1
        quit = input("Enter 'exit' to exit the game - ")
        if(quit=="exit"):
            i =0
            break
        else:
            usr_inp = int(input("Enter number here - "))
            i=1
            continue
    
    print("Thanks for Playing the game. Your Score was - ",count)


usr_inp = int(input("Enter the number of your choice btween 1-9 - "))

random_guess(usr_inp)