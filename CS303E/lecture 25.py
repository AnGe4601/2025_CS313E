'''
def linear_search(lst, target):
    for i in range(len((lst))):
        if lst[i] == target:
            return i
    return -1

def main():
    lst = [-1, 2, 6, 12, 37, 41, 72, 88, 90]
    print(linear_search(lst, 41))

main()

def binary_search(lst, target):
    middle = len(lst) / 2
    for i in range(middle):
        if lst[i] == target:
            return i
        elif i > target:
            for i in (middle, lst[-1] + 1):
'''
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    
    while high >= low: # eventually there will be a flip flop situation 
        mid = (low + high) // 2  # to avoid having float and it always rounds down
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid - 1 

def main():
    lst = [-1, 2, 6, 12, 37, 41, 72, 88, 90]
    print(binary_search(lst, 41))

main()
