def removing_list_loop(list):
    final_list=[]
    for i in list:
        if i not in final_list:
            final_list.append(i)
        else:
            continue
    print(final_list)
    return final_list



def remove_list_sets(list):
    uni_list = set(list)
    return uni_list




list_size = int(input("Enter size of list - "))
i=0
usr_list = []
while(i<list_size):
    a = int(input("Enter the list number - "))
    usr_list.append(a)
    i+=1

print(remove_list_sets(usr_list))

print(removing_list_loop(usr_list))


