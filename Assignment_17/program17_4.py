#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number returns addition of its factorial
#   Author              :   Ankur Takale
#
#===================================================================================================

import sys

def AdditionFact(No):

    Add = 0

    for i in range(1,(No//2)+1):
        if (No%i) == 0:
            Add = Add + i

    return Add

def main():
    Ret = 0
    
    sys.set_int_max_str_digits(Ret)

    No = int(input("Enter number : "))

    Ret = AdditionFact(No)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()