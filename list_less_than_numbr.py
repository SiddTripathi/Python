def listLessThan(list,num):
    final_list = [i for i in list if i<num]
    return final_list



lst_size = int(input("Enter the size of list you want to create - "))
numb_comp = int(input("Enter a number for comparison - "))
usr_lst = []
while(lst_size!=0):
    a = int(input("Enter a number in lst - "))
    usr_lst.append(a)
    lst_size-=1

print(listLessThan(usr_lst, numb_comp))

