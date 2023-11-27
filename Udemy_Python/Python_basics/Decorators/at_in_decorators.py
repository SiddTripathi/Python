user = {"username":"jose","access_level": "guest"}
import functools



def make_secure_function(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] =="admin":
            return func()
        else:
            return f"No admin permissions to {user['username']}"
    return secure_function


@make_secure_function
def get_password():
    return 1234




print(get_password())
print(get_password.__name__)