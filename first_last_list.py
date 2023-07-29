def first_last(list1):
    print("The first element of list",list1[0])
    print("The last element of list", list1[-1])


usr_length = int(input("Enter the list of - "))
list1= []
while(usr_length<0):
    a = int(input("Enter the first element - "))
    list1.append(a)
    usr_length-=1

first_last(list1)