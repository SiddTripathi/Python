#List Sets and Tuple

#Lists - a standard collection of items which can be modified and can have duplicate elemnts. Lists are ordered and items of list can be accessed using that order (index) []

even_num = [2,4,6,8,10]
print(f"List index starts from zero so first element is at zero index - {even_num[0]}")

print(f"We can access list in reverese order by negative index - {even_num[-2]}")

#adding element in list 

#using append, element is added at the end
even_num.append(28)
print(even_num)

#using insert, element added at specific index
even_num.insert(3,24)
print(even_num)

#using extend, add a list of collection or single item at the end
more_even =[12,14,16,18,20]
print(more_even)
more_even.extend(even_num)
print(more_even)


#Tuples - are like lists but cannot be chnaged or modified once created. ()

my_tuple =('Sidd','Prkhar','Shkti')
num_tuple = (50,)  # - tuple with element. if no comma then python cannot compilte brackets number

print(num_tuple)
print(my_tuple)

#Sets -  are collection of items. Not ordered and does not allow duplicate items. {}

#adding elements in sets - since its unordered just have one method called add

my_cars = {'Omni','Alto','WagonR','Grand Vitara'}
print(my_cars)
my_cars.add('Baleno')
my_cars.add('Omni') # Notice that Omni wont be added but Baleno will be
print(my_cars)





#Advanced Sets functions -



# difference - removes common elements from both sets and gives u difference

set_a = {'Car','Bike','Aeroplane','Tank'}
set_b = {'Car','Bike'}

print(set_a.difference(set_b))
print(set_b.difference(set_a)) #Now remember, there is no negative in sets so A-B will be null if all elements of A are in B. So do b.difference(a)

#intersection - gives you the common elements if any between two sets
set_b.add('Bycycle')
print(set_a.intersection(set_b))

#union combines the elements of both sets and give one set
print(set_a.union(set_b))

