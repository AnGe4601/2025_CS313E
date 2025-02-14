def rotate_list(num_list, shift_n):
    if len(num_list) == 0:
        return num_list
    
    new_list = [0] * len(num_list)
    for i in range(len(num_list)):
        mew_i = (i + shift_n) % len(new_list)
        new_list[new_i] = num_list[i]

        return new_list
        
def main():
    num_list = [1, 2, 3, 4]
    shift_n = 2
    roatet_list(num_list, shift_n)
