def palindromCheck(string):
    if(string[::]==string[::-1]):
        print("The String %s is a Palindrom" %(string))
    else:
        print("%s is not a Palindrom"%(string))


usr_string = input("Enter string to check if it is Palindrom - ")
palindromCheck(usr_string)