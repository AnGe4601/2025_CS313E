import string
print(string.punctuation)
print(type(string.punctuation))

punctuation = set()
for i in string.punctuation:
    punctuation.add(i)
print(punctuation)




'''
    for lines in input_file:
        lines = lines.lower().strip().split()
        print(lines)

    for i in range(len(lines)):
            for j in lines[i]:
                if i not in stop_words:
                    valid_word = ""
                if j not in punctuation:    
                    valid_word += j
                    if valid_word not in word_count:
                        word_count[valid_word] = 1
                    else:
                        word_count[valid_word] += 1
        print(word_count)
    '''
