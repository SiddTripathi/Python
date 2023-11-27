user = {"username":"jose","access_level": "admin"}
import functools



def make_secure_function(func):
    @functools.wraps(func)
    def secure_function(*args,**kwargs):
        if user["access_level"] =="admin":
            return func(*args,**kwargs)
        else:
            return f"No admin permissions to {user['username']}"
    return secure_function


@make_secure_function
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super strong password"
    




print(get_password("billing"))
print(get_password.__name__)