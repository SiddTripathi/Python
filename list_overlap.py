

def common_list(list1,list2):
    final_list=[]
    final_list = [i for i in list1 if (i in list2 and i not in final_list)]
    list1_set = set(list1)
    list2_set = set(list2)
    final_list_set = list1_set.intersection(list2_set)

    print("Number of common elements in lists", len(final_list))
    print("The common elements are - ",final_list_set)
    print("The common elements in two lists - ", final_list)


length_list1 = int(input("Enter the size of list1 - "))
list1=[]
while(length_list1>0):
    a = int(input("Enter element of list1 - "))
    list1.append(a)
    length_list1-=1
length_list2 = int(input("Enter the size of list2 - "))
list2 = []
while(length_list2>0):
    b = int(input("Enter a number in list2 - "))
    list2.append(b)
    length_list2-=1

common_list(list1,list2)