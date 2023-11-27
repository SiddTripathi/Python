def search(sequence,expected,finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find name {expected} in sequence")


def friend_find(friend):
    return friend["name"]

friends = [
    {"name":"Prakash","age":23},
    {"name":"Raunac","age":24},
    {"name":"Smita","age":21},
]



try:
    name = input("Enter name you want to search: ")
    results =  search(friends,name,friend_find)
except RuntimeError as e:
    print(e)

else:
    print(results)
finally:
    print("The Search program ")