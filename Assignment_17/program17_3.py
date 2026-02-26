#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number returns its factorial
#   Author              :   Ankur Takale
#
#===================================================================================================

import sys

def Factorial(No):

    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Ret = 0
    
    sys.set_int_max_str_digits(Ret)

    No = int(input("Enter number : "))

    Ret = Factorial(No)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()