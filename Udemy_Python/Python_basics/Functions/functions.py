#simple function
#Reusable code

def hello():
    print("Hello I am a Function")

hello()

#Calcualte age in months

def age_in_months():
    age = int(input("Enter you present age: "))
    age_months = age*12
    print(f'You are {age_months} months old')


age_in_months()

#dont use undeclared variable inside a function

friends = ["Rolf","BoB"]

def add_friend():
    friend_name = input("Enter you friends name: ")
#    friends =  friends + [friend_name] -# Error will be thrown - Cannot access local variable with no value
    friends.append(friend_name) #or
    f = friends + [friend_name]
    print(friends)
    print(f)

add_friend()