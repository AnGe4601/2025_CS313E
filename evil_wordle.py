"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my honor, Angela Liu, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: yl42556
"""

import random
import sys

# ANSI escape codes for text color
# These must be used by wrapping it around a single character string
# for the test cases to work. Please use the color_word function to format
# the feedback properly.

CORRECT_COLOR = "\033[3;1;102m"
WRONG_SPOT_COLOR = "\033[3;1;90;103m"
NOT_IN_WORD_COLOR = "\033[3;1m"
NO_COLOR = "\033[0m"

# Used for the explanation.
BOLD_COLOR = "\033[1m"

# If you are colorblind for yellow and green, please use these colors instead.
# Uncomment the two lines below. Commenting in and out can be done by
# highlighting the  lines you care about and using:
# on a windows/linux laptop: ctrl + /
# on a mac laptop: cmd + /

# CORRECT_COLOR = "\033[3;1;97;101m"
# WRONG_SPOT_COLOR = "\033[3;1;97;104m"

# The total number of letters allowed
NUM_LETTERS = 5

INVALID_INPUT = "Bad input detected. Please try again."


class Keyboard:
    """
    The Keyboard class displays and updates a text-based keyboard that prints
    after every guess. The colors of the keyboard letters are updated per guess
    to reflect which guessed letters are correctly placed, incorrectly placed,
    or not present in the secret word.

    Instance Variables:
        rows: A tuple of strings, each strings representing a row of letters on the keyboard.
        colors: A dictionary mapping each letter to its current feedback color.
    """

    def __init__(self):
        """
        Initializes the Keyboard object by setting up the rows of keys and initializing
        each key with a default 'NO_COLOR' state.
        """
        self.rows = ("qwertyuiop", "asdfghjkl", "zxcvbnm")
        self.colors = {letter: NO_COLOR for letter in "qwertyuiopasdfghjklzxcvbnm"}

    def update(self, feedback_colors, guessed_word):
        """
        Updates the color of each letter on the keyboard based on feedback from a guessed word.

        If a letter's feedback color is `CORRECT_COLOR`, the letter on the keyboard
        is updated. If the color is `WRONG_SPOT_COLOR`, the color updates only
        if the keyboard's current color for that letter is not `CORRECT_COLOR`.
        Letters marked with `NO_COLOR` retain that color unless any feedback
        changes it.

        pre:
            feedback_colors: A tuple of color ANSI escape codes indicating
            feedback for each letter. len(feedback_colors) == len(guessed_word).
            Each item in feedback_colors must be a valid color constant.
            guessed_word:  A list of string characters; the word guessed by the user.

        post: None
        """
        for i, letter in enumerate(guessed_word):
            if feedback_colors[i] == CORRECT_COLOR:
                self.colors[letter] = CORRECT_COLOR
            # make sure it only changes when it's not correct color
            elif feedback_colors[i] == WRONG_SPOT_COLOR and self.colors[letter] != CORRECT_COLOR:
                self.colors[letter] = WRONG_SPOT_COLOR
            # never updated before
            elif feedback_colors[i] == NOT_IN_WORD_COLOR and self.colors[letter] == NO_COLOR:
                self.colors[letter] = NOT_IN_WORD_COLOR

    def __str__(self):
        """
        Returns a string representation of the keyboard, showing each letter in its
        corresponding color. Each row of the keyboard is formatted for readability,
        with spacing adjusted for alignment. Color each individual letter using color_word()
        based on the colors in the dictionary.

        The first row has no leading spaces.
        The second keyboard row has 1 leading space.
        The third keyboard row has 3 leading spaces.

        Here is the print format (without the ANSI coloring):

        q w e r t y u i o p
         a s d f g h j k l
           z x c v b n m

        pre: None
        post: Returns a formatted string with each letter colored according to feedback
              and arranged to match a typical keyboard layout.
        """
        display_list = []
        for row in range(3):
            for letter in self.rows[row]:
                if letter in ("p", "l"):
                    display_list.append(color_word(self.colors[letter], letter) + "\n")
                elif letter == "a":
                    display_list.append(" " + color_word(self.colors[letter], letter) + " ")
                elif letter == "z":
                    display_list.append("   " + color_word(self.colors[letter], letter) + " ")
                elif letter == "m":
                    display_list.append(color_word(self.colors[letter], letter))
                else:
                    display_list.append(color_word(self.colors[letter], letter) + " ")
        display = "".join(display_list)
        return display

class WordFamily:
    """
    A class representing a group or 'family' of words that match a specific
    pattern of feedback_colors. Each word family has a difficulty level determined
    by the total feedback_color difficulty and the number of words in the family.

    Class Variables:
        COLOR_DIFFICULTY: A dictionary mapping color codes to numeric difficulty levels.

    Instance Variables:
        feedback_colors: A tuple representing feedback colors for a guessed word
        words: A list of words that match the feedback pattern.
        difficulty: An integer representing the cumulative difficulty of this word family.
    """

    COLOR_DIFFICULTY = {CORRECT_COLOR: 0, WRONG_SPOT_COLOR: 1, NOT_IN_WORD_COLOR: 2}

    def __init__(self, feedback_colors, words):
        """
        Initializes the WordFamily based on the feedback colors list. The
        difficulty of the family is calculated based on the color difficulty of
        each character in the feedback colors.

        pre:
            feedback_colors: A tuple representing feedback colors for a guessed word
            words: A list of words that match the feedback pattern
        post: None
        """
        self.feedback_colors = feedback_colors
        self.words = words
        self.difficulty = 0
        for color in feedback_colors:
            if color is not NO_COLOR:
                self.difficulty += WordFamily.COLOR_DIFFICULTY[color]

    def __lt__(self, other):
        """
        Compares this WordFamily object with another by prioritizing a larger
        number of words, higher difficulty, and lexicographical order of the feedback_color.
        Raises an error if other is not a WordFamily object.

        pre: `other` is a WordFamily object.
        post:
            True if this instance is 'less than' the other, False otherwise.
            raises NotImplementedError with the message: "< operator only valid
            for WordFamily comparisons." if `other` is not a WordFamily instance.
        """
        if not isinstance(other, WordFamily):
            raise NotImplementedError("< operator only valid for WordFamily comparisons.")
        if len(self.words) == len(other.words):
            # higher difficulty
            if self.difficulty == other.difficulty:
                # color (ASCII value)
                if self.feedback_colors < other.feedback_colors:
                    return True
            elif self.difficulty > other.difficulty:
                return True
            else:
                return False
         # larger size more difficult
        elif len(self.words) > len(other.words):
            return True
        return False

    # DO NOT change this method.
    # You should use this for debugging!
    def __str__(self):
        return (
            f"({len(self.words)}, {self.difficulty}, "
            f"{color_word(self.feedback_colors, ['░'] * 5)})"
        )

    # DO NOT change this method.
    def __repr__(self):
        return str(self)

# DO NOT change this function
def print_explanation(attempts):
    """Prints the 'how to play' instructions on the official website"""

    print("Welcome to Command Line Evil Wordle!")
    print()

    print("".join([BOLD_COLOR + letter + NO_COLOR for letter in "How To Play"]))
    print(f"Guess the secret word in {attempts} tries.")
    print("Each guess must be a valid 5-letter word.")
    print("The color of the letters will change to show")
    print("how close your guess was.")
    print()

    print("Examples:")
    print(CORRECT_COLOR + "w" + NO_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "eary"]))
    print(BOLD_COLOR + "w" + NO_COLOR, end=" ")
    print("is in the word and in the correct spot.")

    print(NOT_IN_WORD_COLOR + "p" + NO_COLOR, end="")
    print(WRONG_SPOT_COLOR + "i" + NO_COLOR, end="")
    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "lls"]))
    print(BOLD_COLOR + "i" + NO_COLOR, end=" ")
    print("is in the word but in the wrong spot.")

    print("".join([NOT_IN_WORD_COLOR + letter + NO_COLOR for letter in "vague"]))
    print(BOLD_COLOR + "u" + NO_COLOR, end=" ")
    print("is not in the word in any spot.")
    print()

# DO NOT change this function
def color_word(colors, word):
    """
    Colors a given word using ANSI formatting then returns it as a new string.

    pre:
        colors: A single ANSI escape code color or list of ANSI escape code colors
        words: A string containing the character(s) to be formatted
    post: Returns a string where each character in word is wrapped in the
        corresponding color from colors, followed by NO_COLOR.
    """
    # Guarantee that colors is a list
    # Useful for if colors is a single color
    if isinstance(colors, str):
        colors = [colors]

    assert len(colors) == len(word), "The length of colors and word do not match."

    colored_word = [None] * len(word)
    for i, character in enumerate(word):
        colored_word[i] = f"{colors[i]}{character}{NO_COLOR}"

    return "".join(colored_word)

# DO NOT change this function
def get_attempt_label(attempt_number):
    """
    Generates the label for the given attempt number.

    pre: attempt_number: 1 < attempt_number < 100 and attempt_number is an integer.
    post: returns a string label for a given attempt
    """
    if 11 <= attempt_number <= 12:  # Special case for teens (11th, 12th)
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(attempt_number % 10, "th")

    return f"{attempt_number}{suffix}"

# DO NOT change this function
def prepare_game():
    """
    Prepares the game by setting the number of attempts and loading the initial
    pool of valid words through the file, "valid_guesses.txt." The function also
    handles optional command-line arguments such as a custom number of attempts
    and a debug flag.

    pre: None

    post: Returns a tuple (attempts, valid_words) or raises a ValueError on invalid user
        attempts: The number of tries the user gets before the game automatically ends.
        valid_words: A list of valid guess words and is the initial pool of secret words.
    """

    valid_words_file_name = "valid_guesses.txt"

    # Must have 1 or 2 arguments
    if len(sys.argv) > 3:
        raise ValueError()
    if sys.argv[-1] == "debug":
        valid_words_file_name = "test_guesses.txt"
        sys.argv.pop()

    if len(sys.argv) == 1:
        attempts = 6
    elif sys.argv[1].isnumeric():
        attempts = int(sys.argv[1])
        if not 1 < attempts < 100:
            raise ValueError()
    # Otherwise, must be bad input and returns None instead
    else:
        raise ValueError()

    # Specify "ascii" as its representation (encoding) since it's required by
    # pylint.
    with open(valid_words_file_name, "r", encoding="ascii") as valid_words:
        valid_words = [word.rstrip() for word in valid_words.readlines()]

    return attempts, valid_words

def fast_sort(lst):
    """
    Returns a new list with the same elements as lst sorted in ascending order. You MUST implement
    either merge sort or quick sort. You may not use selection sort, insertion sort, or any other
    sorting method such as the built-in sort() and sorted(). Your sorting function must be able to
    sort lists of WordFamily, integers, floats, and strings. See the test cases for an example.

    pre: Lst: A list of words
    post: Returns a new list that is sorted based on the items in lst.

    """
    if len(lst) <= 1:
        return lst

    pivot = lst[(len(lst) // 2)]
    less, equal, more = [], [], []

    for i in lst:
        if isinstance(i, WordFamily):
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                more.append(i)
        else:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                more.append(i)
    new_lst = fast_sort(less) + equal + fast_sort(more)
    return new_lst

def get_feedback_colors(secret_word, guessed_word):
    """
    * Author: Angela Liu
    * Assignment: Wordle
    Processes the guess and generates the colored feedback based on the potential secret word. This
    function should not call color_word and instead returns the list of colors used for the
    corresponding letters.

    This should be extremely similar to what you have from assignment 3: Wordle.

    pre: secret_word must be a string of exactly 5 lowercase alphabetic characters.
         guessed_word must be a string of exactly 5 lowercase alphabetic characters.
    post: the return value is a list where:
          - Correctly guessed letters are marked with CORRECT_COLOR.
          - Correct letters in the wrong position are marked with WRONG_SPOT_COLOR.
          - Letters not in secret_word are marked with NOT_IN_WORD_COLOR. The list will be of
            length 5 with the ANSI coloring in each index as the returned value.
    """
    feedback = [None] * NUM_LETTERS

    count = {}
    # count how many times have a character appeared
    for char in secret_word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    # correctly guessed at correct spot
    for i in range(NUM_LETTERS):
        char = guessed_word[i]
        if char == secret_word[i]:
            feedback[i] = CORRECT_COLOR
            count[char] -= 1
    # wrong spot or wrong guesses
    for i in range(NUM_LETTERS):
        char = guessed_word[i]
        if feedback[i] is not CORRECT_COLOR:
            if char in secret_word and count[char] > 0:
                feedback[i] = WRONG_SPOT_COLOR
                count[char] -= 1
            else:
                feedback[i] = NOT_IN_WORD_COLOR
    # You do not have to change this return statement
    return feedback


def get_feedback(remaining_secret_words, guessed_word):
    """
    Processes the guess and generates the colored feedback based on the hardest word family. Use
    get_feedback_colors to group the words based on their feedback, and then create word families
    based on these groups. The hardest word family is then chosen by sorting the families, where
    the 0th index is now the hardest word family.

    pre:
        remaining_secret_words: is a list of words
        guessed_word: must be a string of exactly 5 lowercase alphabetic characters
    post: Returns a tuple (feedback_colors, new_remaining_secret_words) where:
          - feedback_colors: a list of feedback colors (CORRECT_COLOR, WRONG_SPOT_COLOR, or
            NOT_IN_WORD_COLOR) that correspond to the remaining secret words
          - new_remaining_secret_words: the remaining secret words, picked by choosing the hardest
            word family, where the hardest word family is decided by these tiebreakers:
            1. Largest word family (length of the word list)
            2. Difficulty of the feedback
            3. Lexicographical ordering of the feedback (ASCII value comparisons)
    """
    # use evreything before
    # first group the words based on their feedback
    # comparing both pattern; feedback_colros = new pattern?
    patterns = {}
    for word in remaining_secret_words:
        feedback_colors = tuple(get_feedback_colors(word, guessed_word))
        if feedback_colors not in patterns:
            patterns[feedback_colors] = [word]
        else:
            patterns[feedback_colors].append(word)
    # create word families based on the groups
    all_patterns = list(patterns.keys())
    potential_word_fam = []
    for pattern in all_patterns:
        potential_word_fam.append(WordFamily(pattern, patterns.get(pattern)))
    # hardest word chosen by sorting the families (fast_sort) -> 0th index
    potential_word_fam = fast_sort(potential_word_fam)
    remaining_secret_words = potential_word_fam[0].words
    feedback_colors = potential_word_fam[0].feedback_colors
    return feedback_colors, remaining_secret_words

# DO NOT modify this function.
def main():
    """
    This function is the main loop for the game. It calls prepare_game() to set up the game,
    then it loops continuously until the game is over.
    """

    try:
        valid = prepare_game()
    except ValueError:
        print(INVALID_INPUT)
        return

    attempts, valid_guesses = valid
    secret_words = valid_guesses

    print_explanation(attempts)

    keyboard = Keyboard()
    attempt = 1

    while attempt <= attempts:
        attempt_number_string = get_attempt_label(attempt)
        prompt = f"Enter your {attempt_number_string} guess: "
        guess = input(prompt)

        # Mimics user typing out the guess when reading input from a file.
        if not sys.stdin.isatty():
            print(guess)

        if guess not in valid_guesses:
            print(INVALID_INPUT)
            continue

        feedback_colors, secret_words = get_feedback(secret_words, guess)
        feedback = color_word(feedback_colors, guess)
        print(" " * (len(prompt) - 1), feedback)

        keyboard.update(feedback_colors, guess)
        print(keyboard)
        print()

        if len(secret_words) == 1 and guess == secret_words[0]:
            print("Congratulations! ", end="")
            print("You guessed the word '" + feedback + "' correctly.")
            break

        attempt += 1

    if attempt > attempts:
        random.seed(0)
        secret_words = fast_sort(secret_words)
        random.seed(0)
        secret_word = random.choice(secret_words)
        formatted_secret_word = "".join(
            [CORRECT_COLOR + c + NO_COLOR for c in secret_word]
        )
        print("Sorry, you've run out of attempts. The correct word was ", end="")

        print("'" + formatted_secret_word + "'.")


# DO NOT change these lines
if __name__ == "__main__":
    main()
