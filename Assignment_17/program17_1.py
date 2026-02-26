#===================================================================================================
#
#   Problem Statement   :   Create one module named as Arithmetic which contains 
#                           4 functions as Add() for addition, Sub() for substraction,
#                           Mult() for multiplicatioj and Div() for division. All 
#                           functions accepts two parameters as number and perform 
#                           the operation. Write python program which call all the 
#                           functions from Arithmetic module by accepting the parameters from user.
#   Author              :   Ankur Takale
#
#===================================================================================================

import Arithmetic

def main():

    print("-"*25)
    
    No1 = int(input("Enter number 1 :  "))
    No2 = int(input("Enter number 2 :  "))

    print("-"*25)

    Ret = Arithmetic.Add(No1, No2)
    print("Addition       : ",Ret)

    print("-"*25)

    Ret = Arithmetic.Sub(No1, No2)
    print("Substraction   : ",Ret)

    print("-"*25)

    Ret = Arithmetic.Mul(No1, No2)
    print("Multiplication : ",Ret)

    print("-"*25)

    Ret = Arithmetic.Div(No1, No2)
    print("Division       : ",Ret)

    print("-"*25)

if __name__ == "__main__":
    main()