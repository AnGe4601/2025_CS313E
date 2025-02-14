# File: HW6.py
# Author: Yingchen (Angela) Liu
# UT EID: yl42556
# Course: CS 303E
#
# Takes files contained words. Program has available functions for different 
# performances and return respective values. Functions includes counting
# words frequency, finding most frequent word, finding same or different
# words from multiple files. 

import string

stop_words = {"a", "am", "an", "and", "are", "as", "at", "be", "but", "by",
              "for", "i", "if", "in", "into", "is", "it", "its", "my", "nor",
              "not", "of", "on", "or", "so", "than", "that", "the", "then",
              "this", "to", "too", "will", "with"}

def count_words(filename):
    '''
    Count the frequency of all the words in a text file

    Parameters
    ----------
    filename : str
        Inputted document of words for counting frenquency
        
    Returns
    -------
    word_counts : dict
        Dictionary of contained words and their appeared frequency
    '''
    input_file = open(filename, 'r')
    word_counts = {}
    file_contents = input_file.read()
    file_contents = file_contents.lower().strip().split()
     
    for i in range(len(file_contents)):
        word = ""
        for j in file_contents[i]:
            if j not in string.punctuation:
                word += j
        if word not in stop_words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1          
    input_file.close()
    return word_counts
  
def find_max(word_counts):
    """
    Find the most frequent word inside a file
    
    Parameters
    ----------
    word_count : dict
        Dictionary of words with their frequency
    
    Returns
    -------
    max_words : tuple
        Tuple contained both the word and its frequency
    """
    max_word = ["word", 0]
    for key, elem in word_counts.items():
        if elem > max_word[1]:
            max_word[0], max_word[1] = key, elem
    max_word = tuple(max_word)
    return max_word

def find_same_words(set1, set2):
    """
    Find words that appeared on both word lists

    Parameters
    ----------
    set1 : set
        A set of words from the first inputted file 
    set2 : set
        A set of words from the second inputed file

    Returns
    -------
    same_words : set
        A set of common words that appeared on both files 
    """
    same_words = set1 & set2
    return same_words
    
def find_different_words(set1, set2):
    """
    Finding words that are in the first file but not in the second

    Parameters:
    -----------
    set1 : set
        A list of words from the first file 
    set2 : set
        A list of words from the second file 

    Returns:
    --------
    differences : set
        A set of words that only exist in the first file 
    """
    differences = set1 - set2
    return differences 

def main():
    raven_word_counts = count_words("raven.txt")
    road_word_counts = count_words("road.txt")
    
    raven_max_word = find_max(raven_word_counts)
    print(f"Count of \"{raven_max_word[0]}\" is: {raven_max_word[1]}")
    print(f"Count of \"nevermore\" is: {raven_word_counts.get('nevermore')}")
    print(f"Count of \"raven\" is: {raven_word_counts.get('raven')}\n")
    
    set1 = set(raven_word_counts.keys())
    set2 = set(road_word_counts.keys())
    same_words = find_same_words(set1, set2)
    
    set2 = set(raven_word_counts.keys())
    set1 = set(road_word_counts.keys())
    differences = find_different_words(set1, set2)
    print(f"{same_words}\n")
    print(f"{differences}")
    
if __name__ == '__main__':
    main()
