def check_primality(usr_numb):
    for i in range(2,usr_numb):
        if(usr_numb%i==0):
            j=1
            break
        elif(usr_numb%i!=0 and usr_numb%usr_numb==0):
            j=0
            continue
    if(j==0):
        print("The number is Prime")
    else:
        print("Number is not Prime")
        

usr_num =  int(input("Enter the number you want to check - "))
check_primality(usr_num)

