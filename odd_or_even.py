def oddEven(num,check):
    if(num%2==0):
        if(num%4==0):
            print(num," is an even number and multiple of 4")
        else:
            print(num," is an even number")
    elif(num%2!=0):
        print(num," is an odd number")
    if(num%check==0):
        print("%d divides %d completely" %(check,num))
    else:
        print("%d does not divides %d completely" %(check,num))



numb =  int(input("Enter a number to check even/odd = "))
divisor = int(input("Enter Check to divide completely - "))
oddEven(numb,divisor)
