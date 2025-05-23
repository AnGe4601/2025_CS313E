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

# the constant used to calculate the step size
STEP_SIZE_CONSTANT = 3


# DO NOT modify this function.
def is_prime(n):
    """
    Determines if a number is prime.

    pre: n is a positive integer.
    post: Returns True if n is prime, otherwise returns False.
    """
    if n == 1:
        return False

    limit = int(n**0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# DO NOT modify this function.
def hash_word(s, size):
    """
    Hashes a lowercase string to an index in a hash table.

    pre: s is a lowercase string, and size is a positive integer representing either
         hash table size or the constant for double hashing.
    post: Returns an integer index in the range [0, size - 1] where the string hashes to.
    """
    hash_idx = 0
    for c in s:
        letter = ord(c) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

def step_size(s):
    """
    Calculates step size for double hashing using STEP_SIZE_CONSTANT.

    pre: s is a lowercase string.
    post: Returns the calculated step size as an integer based on the provided string.
    """
    key_value = hash_word(s, STEP_SIZE_CONSTANT)
    return STEP_SIZE_CONSTANT - (key_value % STEP_SIZE_CONSTANT)

def insert_word(s, hash_table):
    """
    Inserts a string into the hash table using double hashing for collision resolution.
    No duplicates are allowed.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Inserts s into hash_table at the correct index; resolves any collisions
          by double hashing.
    """
    key_value = hash_word(s, len(hash_table))
    if find_word(s, hash_table):
        return
    # collide
    if hash_table[key_value] != (""):
        step = step_size(s)
        new_key_value = (key_value + step) % len(hash_table)
        while hash_table[new_key_value] != ("") and new_key_value < len(hash_table):
            new_key_value = (new_key_value + step) % len(hash_table)
        hash_table[new_key_value] = s
    else:
        hash_table[key_value] =  s

def find_word(s, hash_table):
    """
    Searches for a string in the hash table.
    Note: using the `in` operator is incorrect as that will be O(N). We want
          an O(1) time average time complexity using hashing.

    pre: s is a string, and hash_table is a list representing the hash table.
    post: Returns True if s is found in hash_table, otherwise returns False.
    """
    key_value = hash_word(s, len(hash_table))
    while hash_table[key_value] != "" and key_value < len(hash_table):
        if hash_table[key_value] == s:
            return True
        # rehash index
        key_value = (key_value + step_size(s)) % len(hash_table)
    return False

def is_reducible(s, hash_table, hash_memo):
    """
    Determines if a string is reducible using a recursive check.

    pre: s is a lowercase string, hash_table is a list representing the hash table,
         and hash_memo is a list representing the hash table
         for memoization.
    post: Returns True if s is reducible (also updates hash_memo by
          inserting s if reducible), otherwise returns False.
    """
    # s doesn't contain a, i, o
    if "a" not in s and "i" not in s and "o" not in s:
        return False
    # s is a, i, o
    if len(s) == 1 and s in ("a", "i", "o"):
        return True
    # s is in hash_memo
    if find_word(s, hash_memo):
        return True
    # s is not a valid word
    if not find_word(s, hash_table):
        return False
    # check if reducible
    for i in range(len(s)):
        if is_reducible(s[:i] + s[i+1:], hash_table, hash_memo):
            insert_word(s, hash_memo)
            return True
    return False

def get_longest_words(string_list):
    """
    Finds longest words from a list.

    pre: string_list is a list of lowercase strings.
    post: Returns a list of words in string_list that have the maximum length.
    """
    longest_word = []
    longest_len = 0
    for word in string_list:
        if len(word) > longest_len:
            longest_word = []
            longest_word.append(word)
            longest_len = len(word)
        elif len(word) == longest_len:
            longest_word.append(word)
    return longest_word

def main():
    """The main function that calculates the longest reducible words"""
    # create word_list
    word_list = []
    try:
        while True:
            word = input()
            word_list.append(word.strip())
    except EOFError:
        pass
    # create hash_list and populate words into hash_list
    n = 2 * len(word_list) + 1
    while not is_prime(n):
        n += 2
    hash_list = []
    for _ in range(n):
        hash_list.append("")
    for word in word_list:
        insert_word(word, hash_list)

    hash_memo = []
    m = round(0.2 * len(word_list) + 1)
    while not is_prime(m):
        m += 2
    for _ in range(m):
        hash_memo.append("")

    reducible_words = []
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
    # find and print out the longest reducible_words
    longest_word_lst = get_longest_words(reducible_words)
    for word in longest_word_lst:
        print(word)

if __name__ == "__main__":
    main()
