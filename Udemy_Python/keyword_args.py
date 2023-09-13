def named(**kwargs):
    print(kwargs)
   
    for key, value in kwargs.items():
        print(key,value)


names = {'name':'bob','age':34}
named(**names)