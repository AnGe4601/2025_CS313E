# File: HW4.py
# Author: Yingchen (Angela) Liu
# UT EID: yl42556
# Course: CS 303E
#
# This program takes user input and implant a designated function that helps to
# determine whether or not the input number is a prime number. It will also
# print out all the pairs or twin primes that are less than 1000 by using
# the designated function. 

def is_prime(num):
    """
    Determines whether or not a number is a prime number

    A prime number should be greater than 1 and can only be exactly devided by
    itself and 1. This function would first check if num is a positive integer
    and is not 1 or 0. It then checks if the num can only be divided by itself
    and 1. If num doesn't meet neither conditions, num is also a prime number
    and function returns False. 
    
    Parameters
    ----------
    num : int
        Any integer input from the user 
        
    Returns
    ----------
    return1 : bool
        True; if it's a prime number 
    return2 : bool
        False; if it's not a prime number 
    """
    if num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                if num == i:
                    return True
                else:
                    return False
    else:
        return False 
            
# following are the test cases to check for the functionality of function is_prime        
def main():
    print(is_prime(7))
    print(is_prime(0))
    print(is_prime(913))
 
#main()

 
def twin_primes():
    """
    Prints out all the pairs of twin primes that are less than 1000.

    Parameters
    ----------
    prime1 : int
        first prime number between the range of 1 to 1000
    prime2 : int
        second prime number and is grater than prime1 by 2

    Returns
    ----------
    return : str
        print statement that has a pair of prime numbers
    """
    for prime1 in range(1, 1001):
        if is_prime(prime1):
            prime2 = prime1 + 2
            if is_prime(prime2):
                print(f"{prime1},{prime2}")

# following are the test cases to check for the functionality of function twin_primes              
def main():
    twin_primes()

#main()
         
        


    
