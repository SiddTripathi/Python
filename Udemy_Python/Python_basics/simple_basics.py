#simple app on strings formating input functions etc

user_age = int(input("Enter you age: "))

age_in_months = user_age*12
age_in_seconds = age_in_months*30*24*60*60*60

print(f"Your age in months is - {age_in_months}")
print(f"Your age in seconds is - {age_in_seconds}")