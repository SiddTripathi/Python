import datetime


def whenHundred(age, num_print):
    curr_year = datetime.datetime.now()
    print(curr_year.year)
    year_of_hund = (100 - age) + curr_year.year
    while (num_print > 0):

        print("The year you will turn 100 is  - ", year_of_hund)
        num_print -= 1


age = int(input("Enter you present age"))
num_print = int(input("Enter number of times you want to print your age - "))
whenHundred(age, num_print)
