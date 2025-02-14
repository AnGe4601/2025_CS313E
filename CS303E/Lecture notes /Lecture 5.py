# another way: print("The area is", round(area, 1))

radius = eval(input("what is the radius? "))
# radius = float(input("what is the radius? )) 
area = 3.14 * (radius ** 2)
area_rounded = round(area, 1)

print("The area of the circle is" + str(area_rounded) + ".")

# importing libraries 
import math
import random 

value = 89
print(math.sqrt(value))

from random import randrange
from random import *    # this one might caused confusion so no recommend 
from random as rd

1. 
F-strings
print(f"Hello World!")

2.
name = "Taylor"
print(f"Hello, {name}!")

print(f"My annual salary is ${annual_pay:.2f}")
