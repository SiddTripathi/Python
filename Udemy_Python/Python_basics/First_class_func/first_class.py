import sys

sys.path.append('D:\\Python\\Python\\')

from Udemy_Python.Python_basics.add_module import divide



def calculate(*values,operator):
    return operator(*values)

result = calculate(20,5,operator=divide)
print(result)
