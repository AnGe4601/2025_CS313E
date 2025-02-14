'''
secret_word_list = []
for i in secret_word:
    secret_word_list.append(i)
guessed_answer_line = len(secret_word_list) * "-"

        if user_guess not in secret_word:
            if user_guess in wrong_guesses:                      
                print(f"You've already guessed {user_guess}")
                user_guess = input("Guess a letter: ")
                
            else:                       
                total_attempts -= 1
                user_guess = input("Guess a letter: ")
                wrong_guesses.append(user_guess)
        
      
        if user_guess in secret_word:
            if guessed_answer_line == secret_word:
                    total_attempts = -1
                    print(str(secret_word))
                    print("You win!")
                        
            else:
                for i in range(len(secret_word)):
                    result = []
                    if user_guess == secret_word[i]:
                        result.append(user_guess)
                    else:
                        result.append("-")
                print(str(result))
 
secret_word = "hi"
print(secret_word[0])


 
                if user_guess != secret_word[i]:
                    total_attempts -= 1
                    right_guesses[i] = 0
                else:
                    right_guesses[i] = 1
                    test = 1
 
if user_guess in right_guesses:
            print(f"You have {total_attempts} tries remaining.")
            if result == secret_word:
                total_attempts = -1
                print("You win!")      
        else:
            total_attempts -= 1
            print(f"You have {total_attempts} tries remaining.")
            if total_attempts == 0:                                    
                print(f"You lose. The word was {secret_word}.")
'''

lst = [0,1,1]
for i in range(len(lst)):
    print(bool(i))
