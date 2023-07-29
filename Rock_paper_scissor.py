import random


def rock_paper(usr_input):
    comp_choice = ['r','p','s']
    
    usr_dict = {"rock":"r","paper":"p","scissor":"s"}
    
    status = 0
    
    while (status==0):
        comp_select = random.choice(comp_choice)
        print(comp_select)
        human_player = usr_dict[usr_input]
        if(comp_select=="r" and human_player =="s"):
            print("Computer has won ! Try again")
        elif(comp_select=="s" and human_player =="p"):
            print("Computer has won ! Try again")
        elif(comp_select == human_player):
            print("Its a Tie !!")
        else:
            print("Human has won")
        check = input("Another round - Enter Y or N - ")
        if(check=="y"):
            status = 0
            usr_input = input("Enter you choice from Rock Paper or Scissor - ")
            continue
        else:
            status = 1
            print("Thank you for Playing")
            break


usr_input = input("Enter you choice from Rock Paper or Scissor - ")
rock_paper(usr_input.lower())
    
    