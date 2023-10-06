#Boolean in Python

print(5==5)
print(5==9)
print(10!=9)

#its like comparison which returns true or false. Another thing is 'is' keyword

a =[1,2,3]
b=[1,2,3]

print(a is b)
print(a[1] is b[1]) 

#if statements

capital = input("Enter City Name: ")

if capital == "New Delhi":
    print("That is India")
elif capital == "Washington DC":
    print("That is America")
elif capital == "Wellington":
    print("That is New Zealand")
else:
    print("Not a Capital city")
print("Thanks for trying") 



#If Statmenets with 'in' keywords

watched_movie  = ["the matrix","zombieland","avatar","titanic"]

usr_movie = input("Enter the Movie you watched: ").lower()

if usr_movie in watched_movie:
    print("I have seen this movie too!!")
else:
    print("Not seen this one")

