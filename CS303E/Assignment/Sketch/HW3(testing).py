# HW3.py
# Author: Yingchen Liu
# UT EID: yl42556
# Course: CS 303E
#
# This is assignemnt 3

# Creating a game called "Guess the Number"
import random as r

#secret_num = r.randint(0, 1000)
secret_num = 458
total_guess = 0
user_answer = -1

print("I'm thinking of a number from 1 to 1000. Try to guess my number!" \
          " (Enter 0 to stop playing.)")
user_answer = int(input("Please enter your guess: "))


while secret_num != user_answer and user_answer != 0:
    
    if user_answer < secret_num:
            total_guess += 1
            print("Your guess is too low.")

    elif user_answer > secret_num:
            total_guess += 1
            print("Your guess is too high.")
         
    elif user_answer < 1 or user_answer > 1000:
            total_guess += 1
            print("Your guess must be between 1 to 1000.")
            
    user_answer = eval(input("Please enter your guess: "))
            
if user_answer == 0:
    print("Goodbye!")
 
# when the user guessed the right answer
if secret_num == user_answer:
    total_guess += 1
    print("That's correct! You win!")
    print(f"You guessed my number in {total_guess} guesses.")

             

