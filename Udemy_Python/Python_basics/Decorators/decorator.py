user = {"username":"jose","access_level": "guest"}


def get_password():
    return 1234

def make_secure_function(func):
    def secure_function():
       if user["access_level"] == "admin":
           return func()
    return secure_function

get_password = make_secure_function(get_password)


print(get_password())