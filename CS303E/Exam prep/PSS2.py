'''
# Question 1
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
 
sum = num1 + num2

if num1 > num2:
    print(f"The sum of all the integers from {num2} to {num1} is {sum}.")
else:
    print(f"The sum of all the integers from {num1} to {num2} is {sum}.")
 
total = 0

for i in range (num1, num2 + 1):
    total += i
    #if num1 > num2:
        #print(f"The sum of all the integers from {num2} to {num1} is {total}.")
    #else:
        #print(f"The sum of all the integers from {num1} to {num2} is {total}.")
    if num1 > num2:
        num1, num2 = num2, num1
 
# Question 2
year = int(input("What year are you curious about? "))

hundred = year / 100
hundred_check = round(hundred, 0)

four_h = year / 400
four_h_check = round(four_h, 0)

if four_h == four_h_check:
    print(f"{year} is a leap year.")
    if  hundred_check == hundred_check and :
        print(f"{year} is not a leap year.")
    
# Question 2 answer 1

year = int(input("What year are you curious about? "))

if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
 
# Question 2 answer 1
year = int(input("What year are you curious about? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
         print(f"{year} is not a leap year.")
else:
     print(f"{year} is not a leap year.")
 
# Question 3
abbrevia = input("Test lingo: ")
trans = f"Translation: "

if abbrevia == "lol":
    print(f"{trans} laugh out loud")
elif abbrevia == "brb":
    print(f"{trans} be right back")
elif abbrevia == "nbd":
    print(f"{trans} no big deal")
elif abbrevia == "idk":
    print(f"{trans} I don't know")
# or
abbrevia = input("Test lingo: ")

lol = laugh out loud
brb = be right back
nbd = no big deal
idk = "I fon't know" 
 
# Question 4:
num = int(input("What is your non-negative integer? "))
total = 1

for i in range(1, num + 1):
    total *= i     # total = total * i
print(f"{num}! is {total:,}.")
'''
# Question 8:


    
