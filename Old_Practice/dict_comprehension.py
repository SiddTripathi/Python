
users = [(0,"Bob","psswrd1"),
         (1,"Tim","psswrd2"),
         (2,"Cook","psswrd3")]


username_mapping = {user[2]:user for user in users}

print(username_mapping)

#Kwargs

def named(**args):
    print(args)


details = {"name":"bob","age":26}

named(**details)

