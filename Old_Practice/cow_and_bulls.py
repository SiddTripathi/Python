import random

def num_gen(digit):
    num = [random.randint(0,9) for i in range(digit)]
    return str(num)

def game(usr_input,usr_digit):
    comp_num = num_gen(usr_digit)
    cow=0
    Bull=0
    count =0 
    for i in usr_input:
        for j in comp_num:
            if i==j:
                cow+=1
                print("You guessed correctly")
            elif i!=j:
                Bull+=1
                print("You Guessed incorrectly")
    if(cow==4):
        print("You have won.")

   


        