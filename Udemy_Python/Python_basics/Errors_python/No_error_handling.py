#This program is just a normal function where exceptional condition is not handled properly. A trivial problem in divide function to handle divisor = 0 condtion
#Now in below program, it will print error and can be relatable. 


def divide(dividend,divisor):
    if divisor==0:
        print("Divisor cannot be 0")
        return
    return dividend/divisor


print(divide(15,0))


#However sometimes, the print statemnt might not make sense to context.See below

grades =[]

average =  divide(sum(grades),len(grades)) #here, user won't understand the context as he is expecting something related to grades. 

#One way of this could be taking out the logic of divisor=0 from function and put it before calling function something -
# if len(grades) == 0:
     #print('Divsor zero')  --> but this looks little messy. Hence we use exception/error handling in Pythoon
     