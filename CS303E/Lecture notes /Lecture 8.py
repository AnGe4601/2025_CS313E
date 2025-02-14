'''
regular = "$15"
senior = "$10"
children = "$10"

day = input("What day is the movie? ")
age = int(input("What is the person's age? ")) 


if age >= 65:
    ticket_price = 10
    if day == "Senior Citizen Discount Days":
        ticket_price = 7
elif age <= 10:
    ticket_price = 10
else:
    ticket_price = 15


print(f"The price of the ticket is ${ticket_price}.")

# Method 2
if age <= 10:
    if day == "Thusday":
        price = 7
    else:
        price = 10
elif age >= 65:
    if day = "Thursday" or day == "Monday":
        price = 7
    else:
        price = 10


# for loop
for i in range(3):
    print("Hello,")
    print("World!")
    
# practice 
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
user_answer = int(input(f"{num1} + {num2} = "))
correct_answer = num1 + num2
begin = 0

for i in range(5):
    user_answer = int(input(f"{num1} + {num2} = "))
    if user_answer == correct_answer:
        print("Great Job!")
        correct_times = begin + 1
        print(f"Correct times:{correct_times}")
    else:
        print("Sorry, nice try.")
 
# lecture example 
import random

score = 0 

for i in range(5):                 # have to include the random number in the loop or will just generate 1 number
    
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    user_answer = int(input(f"{num1} + {num2} = "))
    correct_answer = num1 + num2

    if user_answer == correct_answer:
        print("Great job")
        score += 1 
    else:
        print("Sorry, nice try.")
        
print(f"The score is {score}.")
 
# my version :(
word = input("String: ")
e_count = 0

for i in word:
    if i == "e" or i == "E":
        e_count += 1
    print(f"\"E\" cpimt is {e_count}")
'''  
# the master piece 
user_input = input("String: ")
e_count = 0 

for char in user_input:
    if char == "e" or char == "E":
        e_count += 1
        
    
