
import string
import random

def gen_pwd(pwd_strngth):
    if(pwd_strngth=='weak'):
        print("You have choosen weak password strength")
        pwd_list = ["Mypass123", "Strong23","Passwrd23"]
        pwd = random.choice(pwd_list)
        print("The password generated is - ",pwd)
    elif(pwd_strngth=='strong'):
        pswrd_lngth = int(input("Enter length of pwd u would like - "))
        lower_case = list(string.ascii_lowercase)
        upper_case = list(string.ascii_uppercase)
        numbs = list(string.digits)
        spcl_chars = list(string.punctuation)
        tmp_pass = random.choice(lower_case) + random.choice(upper_case) + random.choice(numbs) + random.choice(spcl_chars)
        comb_list = lower_case + upper_case + numbs + spcl_chars
        
        pas_list = []
        lngth=pswrd_lngth-4

        while(lngth>0):
            temp = random.choice(comb_list)
            pas_list.append(temp)
            lngth-=1
        
        final_pass = tmp_pass + "".join(pas_list)
        print("Your Final password - ",final_pass)


psswrd_strnth = input("Enter weak or strong for strength - ").lower()

gen_pwd(psswrd_strnth)

