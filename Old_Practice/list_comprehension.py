def evenList(lst1):
    even_list = [i for i in lst1 if i%2==0]
    return even_list


size_list = int(input("Enter size of list - "))
usr_lst = []
while(size_list!=0):
    usr_lst.append(int(input("Enter a number in list - ")))
    size_list-=1

print(evenList(usr_lst))
