
friends_age = {"Ramesh":29,"Suresh":30,"Rajesh":32}
print(friends_age)
friends_age["Ramesh"] = 34
print(friends_age)


friends = [
    {"name":"Sidd", "age":23},
    {"name":"Prak","age":24},
    {"name":"Rishi","age":25}
]


print(friends[1]["name"])
print(friends[0]["age"])
    
friends_attendance = {"Rishi":96,"Raj":80,"Anne":100}

for name,attendance in friends_attendance.items():
    if attendance==100:
        print(f"{name} has {attendance} attendance which is hghest. Well Done")
    else:
        print(f"{name} has {attendance} attendance")


print(friends_attendance.keys())
print(friends_attendance.values())
print(sum(friends_attendance.values())/len(friends_attendance.values()))

lets_try = {1:"Sidd",2:"Rishi"}

print(lets_try.keys())
print(lets_try.values())