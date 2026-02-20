#===========================================================================
#
#   Problem Statement   :   Write a program which contains a function and it 
#                           takes two numbers as input and returns addition
#   Author              :   Ankur Takale
#
#===========================================================================

def Addition(No1, No2):

    Ans = No1 + No2

    return Ans

def main():

    Value1 = float(input("Enter number :  "))
    Value2 = float(input("Enter number :  "))

    Ret = Addition(Value1, Value2)

    print("Addition is  : ",Ret)

if __name__ == "__main__":
    main()