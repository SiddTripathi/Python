import random

lst1_size = int(input("Enter the size of first list - "))
lst1 = []
lst2_size = int(input("Enter the size of second list - "))
lst2 = []
while(lst1_size!=0):
    lst1.append(random.randint(10,20))
    lst1_size-=1

while(lst2_size!=0):
    lst2.append(random.randint(12,24))
    lst2_size-=1

final_lst = []
for i in lst1:
    for j in lst2:
        if(i==j and i not in final_lst):
            final_lst.append(i)

print(lst1)
print(lst2)
print(final_lst)