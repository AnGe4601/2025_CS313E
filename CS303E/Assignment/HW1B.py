# File: HW1B.py
# Author: Yingchen Liu
# UT EID: yl42556
# Course: CS 303E
#
# This is part B of Assignment 1

# Greeting users
name = input("What is your name? ")
print("Hello", name + "!", "You have just delved into Python.\n")

# Converting input temperature in Celsius to Fahrenheit
c_temp = input("Enter a temperature in degrees Celsius: ")
f_temp = 9 / 5 * int(c_temp) + 32
print(c_temp, "Celsius is", f_temp, "Fahrenheit.\n") 

# Calculating the total amount of a bill with gratuity 
bill, g_rate = eval(input("Enter the bill and gratuity rate: "))
gratuity = bill * (g_rate / 100)
total = gratuity + bill
print("The gratuity is $" + str(round(gratuity, 2)),  "and the total is $" \
      + str(round(total, 2)) + ".\n")
 
# Calculating the sum of the digits of an integer between the amount of 0 to 999
num = int(input("Enter a number between 0 and 999: "))
ones = num % 10 
tens = round(num % 100 // 10)
huns = round(num % 1000 // 100)
sum_d = ones + tens + huns 
print(f"The sum of the digits is {sum_d}.\n")
 
# Calculate an investment return by using formula a = p(1 + r) ** n 
p_principle = float(input("Enter your investment amount ($): "))
r_annual_rate = 0.07
n_years = int(input("Enter your investment length (years): "))
a_total = round(p_principle * (1 + r_annual_rate) ** n_years, 2)
print("After " + str(n_years) + " years, you will have $" + str(a_total) + ".\n")

# Calculating the safe range of heart rate
age = int(input("Enter your age: "))
max_rate = 220 - age
min_target = round(max_rate * 0.50)
max_target = round(max_rate * 0.85)
print("Your target heart rate is", min_target, "-", max_target, "bpm.")
