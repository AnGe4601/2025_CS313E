# File: HW5.py
# Author: Yingchen(Angela) Liu
# UT EID: yl42556
# Course: CS 303E
#
# This program will randomly generate a word from designated list for playing
# hangman. It will first evaluate user's guesses and then display result.

import random

def load_words(filename):
    """
    Creates a list of words from the file contents

    Parameters
    ----------
    filename : str
        Name of the file to be processed, contains a single word on each line
    
    Returns
    -------
    word_list : list or str
        List of words, each element is a word from the file
    """
    word_list = []
    try:
        file = open(filename, "r")
        for line in file:
            word = line.strip()
            word_list.append(word)
        file.close()
    except FileNotFoundError:
        print("File not found. Please ensure that 'words.txt' is in the same folder.")
    return word_list

def play_hangman():
    """
    Play hangman (a word-guessing game) with user

    This program will first examine if user input is a letter and have not
    been guessed before. If passed evaluation, the program will check if
    the input matches the generated word (right answer). Only valid
    character will be save to a new list (right_guess) that will be
    reference for printing out the result. Program will give out
    respective responses to each individual result. 
    
    """
    secret_word = random.choice(load_words("words.txt"))
    #secret_word = "banjo"
    print("Let's play hangman!")
    dash_line = len(secret_word) * "-"
    print(dash_line)

    total_attempts = 8
    duplication = []
    right_guesses = []
    for char in range(len(secret_word)):
        right_guesses.append(0)
            
    #Continue prompting user until gussed all characters or run out of attempts
    while total_attempts > 0:
        result = ""   
        user_guess = str.lower(input("Guess a letter: "))
        #check if user input is valid
        if str.isalpha(user_guess) != True or len(user_guess) > 1:
            print("That is not a letter. Enter a letter.")  
        elif user_guess in duplication:
            print(f"You've already guessed {user_guess}")    
        else:
            for i in range(len(secret_word)):
                if user_guess == secret_word[i] and right_guesses[i] == 0:
                    right_guesses[i] = user_guess
            #generate reference for program to print result         
            for i in range(len(right_guesses)):
                if right_guesses[i] == 0:
                    result += "-"
                else:
                    result += right_guesses[i]       
            if user_guess in right_guesses:
                print(result)
                if result == secret_word:
                    total_attempts = -1
                    print("You win!")
                else:
                    print(f"You have {total_attempts} tries remaining.")      
            else:
                total_attempts -= 1
                print(result)
                print(f"You have {total_attempts} tries remaining.")
                if total_attempts == 0:                                    
                    print(f"You lose. The word was {secret_word}.")               
            duplication.append(user_guess)         
          
def main():
    play_hangman()

if __name__ == '__main__':
    main()
       
