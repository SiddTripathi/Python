
import divide_module as calc
import sys
sys.path.append('D:\\Python\\Python\\')
from Udemy_Python.Python_basics.add_module import add  # --> to import modules outside of the parent package (in this case imports folder, 2 options -- 
#a. Set PYTHONPATH in terminal settings file of Visual Studio Code, or Windows environment variable and add PYTHONPATH)
#b. append your extended location to sys.path which is the default location where python interpreter looks for modules. Usually this is inside parent folder
# import sys --> sys.path.append('D:/Python/Python/)


print("bahar wala",add(4,5))

print(calc.divide(8,2))
print(calc.add_module.add.add(4,2))



#its advisable to use import module insttead of from module import. By using import module u dont loose context of function.(unless ofcourse name of function are too obvious)