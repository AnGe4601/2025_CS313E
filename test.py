'''
    for i in range(NUM_LETTERS):
        char = guessed_word[i]
        if char in secret_word and count[char] > 0:
            # right spot
            if char == secret_word[i]:
                feedback[i] = CORRECT_COLOR
                count[char] -= 1
            # wrong spot
            else:
                feedback[i] = WRONG_SPOT_COLOR
                count[char] -= 1
        else:
            # wrong guess
            feedback[i] = NOT_IN_WORD_COLOR
'''
