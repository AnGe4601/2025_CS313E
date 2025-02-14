def linear_search(lst, target):
    for i in range(len((lst))):
        if lst[i] == target:
            return i
    return -1

def main():
    lst = [-1, 2, 6, 12, 37, 41, 72, 88, 90]
    print(linear_search(lst, 41))

main()
