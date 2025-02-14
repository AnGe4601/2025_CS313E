def power(base, exp):
    if exp == 0:
        return 1
    else:
        return power(base, exp - 1) * base
    
def main():
    print(power(2, 1))
    
main()
