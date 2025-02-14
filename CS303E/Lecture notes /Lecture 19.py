'''
#Q1
def replace_words(text, old_word, new_word):
    words = text.split(" ")      #call on a str, split based on whites spaces and turns out to be a list
                                 #however, the split is also taking away all these formating 
    mod_text = []
    for word in words:
        if word == old_words:
            mod_text.append(new_word)
        else:
            mod_text.append(word)
    mod_text = " ".join(mod_text)   #making it a one giant string 

    return mod_text
    
def main():
    file = open("raven.txt", r)
    text = file.read()
    file.close()

    mod_text = replace_words(text, "Raven", "Birdie")
    print(mod_text)

main()
'''
#Q2
def count_letters(word, letter):
    count = 0 
    for char in word:
        if char == letter:
            count += 1

    return count
            
def main():
    print("Num of o's in frivolous is", count_letters("frivolous", "o"))

main() 
    
    
