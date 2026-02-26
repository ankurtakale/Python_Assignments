#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number and checks it is prime or not
#   Author              :   Ankur Takale
#
#===================================================================================================

import sys

def CheckPrime(No):

    Flag = True

    if No <= 1:
        return False

    for i in range(2,(No//2)+1):
        if (No%i) == 0:
            Flag = False
            break
    
    return Flag

def main():
    Ret = 0
    
    sys.set_int_max_str_digits(Ret)

    No = int(input("Enter number : "))

    Ret = CheckPrime(No)

    if Ret == True:
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()