# File: HW2.py
# Author: Yingchen Liu
# UT EID: yl42556
# Course: CS 303E
#
# This is Assignment 2
''' 
# Q1: Calculate the area of a pentagon
import math as m

# Setting up formula and collect user inputs 
radius = float(input("Enter the radius of the pentagon: "))
side_length = 2 * radius * m.sin(m.pi / 5)
area_formula = 5 / (4 * m.sqrt(5 - 2 * m.sqrt(5))) * (side_length ** 2)

print(f"The area of the pentagon is {area_formula:.2f} units squared.\n")
 
# Q2: Printing a payroll statement

# Ask user inputting their information (including name, hours, and tax rates) and calculate gross pay total 
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked this week: "))
pay_rate =  float(input("Enter hourly pay rate: "))
gross_pay = hours * pay_rate
federal_tax_r = eval(input("Enter federal tax withholding rate (%): ")) 
state_tax_r = eval(input("Enter state tax withholding rate (%): ")) 

# Calculate federal, state withholding and net pay          
f_withholding = gross_pay * (federal_tax_r / 100)
s_withholding = gross_pay * (state_tax_r / 100)
net_pay = gross_pay - f_withholding - s_withholding

# Write f-string short-cut for printing 
print_p_r = f"${pay_rate:.2f}"
print_gross = f"${gross_pay:.2f}"
print_f_withholding = f"${f_withholding:.2f}"
print_s_withholding = f"${s_withholding:.2f}" 

print(f"\nWeekly Pay Statement for {name}")
print(f"Hours Worked:{hours:9.1f}")                 
print(f"Pay Rate:{print_p_r:>13}")
print(f"Gross Pay:{print_gross:>12}")            
print("Deductions:")
print(f"  Federal Withholding ({federal_tax_r}%):{print_f_withholding:>8}")
print(f"  State Withholding ({state_tax_r}%):{print_s_withholding:>9}")
print(f"Net Pay: ${net_pay:.2f}\n")
'''
# Q3: Create a rock, paper, scissors game
import random as r
 
user = input("Choose rock, paper, or scissors: ") 
computer =  r.randint(0, 2)

# Write results in f-string
draw = f" You are {user}.\nDraw."
computer_wins = f" You are {user}.\nComputer wins."
user_win = f" You are {user}.\nYou win."

if computer == 0:
    num_to_word = f"Computer is rock."
    if user == "rock":
        print(f"{num_to_word}{draw}")
    elif user == "paper":
        print(f"{num_to_word}{user_win}")
    else:
        print(f"{num_to_word}{computer_wins}")
elif computer == 1:
    num_to_word = f"Computer is paper."
    if user == "rock":
        print(f"{num_to_word}{computer_wins}")
    elif user == "paper":
        print(f"{num_to_word}{draw}")
    else:
        print(f"{num_to_word}{user_win}")
else:
    num_to_word = f"Computer is scissors."
    if user == "rock":
        print(f"{num_to_word}{user_win}")
    elif user == "paper":
        print(f"{num_to_word}{computer_wins}")
    else:
        print(f"{num_to_word}{draw}")

    
