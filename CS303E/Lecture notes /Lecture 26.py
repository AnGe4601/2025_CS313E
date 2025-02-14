'''
lst = []

for i in word:
    lst[0] = i
'''
def reverse_iterative(string):
    # 1 
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    return reversed_string

def reverse_recursive(string):
    # 2 but my version 
    #for i in string:
        #reversed_iterative(string) = i + string.strip[i]
    
    if string == "":
        return ""
    else:
        
        return reverse_recursive([1:]) + string[0] 
    
def main():
    print(reverse_iterative("stresssed"))

if __name__ == "__main__":
    main()
        
