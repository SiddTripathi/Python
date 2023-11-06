#lambda function is somewhat similar to listcomprehension. Only used to produce output not perform any action

print((lambda x,y: x+y)(5,7)) #  - a one line function/Rare usage


#use case for list comprehension

def double(x):
    return x*2

list_1 = [1,2,3,4]

doub_list1 = [double(x) for x in list_1]
print(doub_list1)


#map is another usage of applying function on list

list_2  = [2,4,6,8]

doub_list2 = map(double,list_2)
print(list(doub_list2))

#lambda function can just reduce the line 8-9


doube_list3 = list(map(lambda x:x*3,list_1))
print(doube_list3)

