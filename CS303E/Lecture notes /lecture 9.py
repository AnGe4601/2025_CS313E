'''
#        [0, 1, 2]
#for i in range(3)

num_yrs = int(input("Years? ")
cost = 1000

for i in range(num_yrs):
        cost *= 1.05
              
print(f"{cost}:,.2f}")
'''

import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
user_answer = int(input(f"{num1} + {num2} = "))
correct_answer = num1 + num2

while user_answer == correct_answer:
    print("Great Job!")
if user_answer != correct_answer:
    print("Sorry, nice try.")
