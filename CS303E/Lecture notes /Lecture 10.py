'''
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

total = 0 

for i in range(num1, num2 + 1, 2):
    if i % 2 == 0:
        total += i
    print(total)
 
# Practice Prob 2
 
num =  int(input("Number: "))

for i in range(num, num+1):
    i /= 2
    if i % 0 != 2:
        for i in range(0, num+1, 1):
            print(i)
 
            
num =  int(input("Number: "))
num_times_divide = 0

while num % 2 ==0:
    num_times_divde += 1
    num /= 2

print(num_time_divide)

one = 0

for i in range(3):
    for one in range(5):
        one += 1
        total = 1 * one
        print(f"1 x {one} = {total}")

# another way
for i in range(1, 4):
    
    for j in range(1, 6):
        mult = i * j
        print(f"{i} x {j} = {mult}")
        
    print()
 
for i in range(24):
    for 
'''
for hr in range(24):
    for mn in range(60):
        for sec in range(60):
            print(f"{hr} : {mn} : {sec}")
            
