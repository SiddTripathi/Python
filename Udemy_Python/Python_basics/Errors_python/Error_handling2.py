from Error_handling import divide



students = [
    {"name":"Ram","grades":[75,80]},
    {"name":"Shyam","grades":[]},
    {"name":"Gyan","grades":[80,90]},
]
avg_list = []
for student in students:
    name = ""
    try:
        name =  student["name"]
        grades = student["grades"]
        average = divide(sum(grades),len(grades))
        
    except ZeroDivisionError as e:
        print(f"ERROR! {name} has got no grades")
        print(f"[MATH - ERROR] - {e}")
    else:
        print(f"Average Grade of {name} is {average}")
    finally:
        print(f"Average grade for {student['name']} calculated")
print("Average Grade Done")