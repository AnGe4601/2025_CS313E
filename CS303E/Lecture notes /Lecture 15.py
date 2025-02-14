'''
#1  
def remove_duplicates(lst):
    new_list = []
    for i in range(len(lst)):
        if lst[i] not in new_list:
            new_list.append(lst[i])

    return new_list

# if you don't care about the index 
    for elem in lst:
        if elem not in new_list:
            new_list.append(elem)
        
def main():
    lst = [2, 2, 3, 4, 5, 3, 4, 4]

'''
#3
def remove_duplicates(lst):
    new_list = []
    seen = set()
    for elem in lst:
        if elem not in seen:
            new_list.append(elem)
            seen.add(elem)
    return new_list

# return list(set(lst))

        
def main():
    lst = [2, 2, 3, 4, 5, 3, 4, 4]     


''' 
#2
def double_matrix(matrix):
    for i in range(len(matrix):
        for j in range(len(matrix[i])): # accessing the elemetns inside the row
                if i % 2 == 0: # even
                   matrix[i][j] *= 2
                else:
                    matrix[i][j] = int(str(matrix[i][j]) * 2)
    return matrix 
                

def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]
    matrix = double_matrix(matrix)
    print(matrix)
'''
