#===========================================================================
#
#   Problem Statement   :   Program to print square of a number using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Square = lambda no : no * no

def main():
    Value = float(input("Enter number : "))

    Ret = Square(Value)

    print("Square : ",Ret)

if __name__ == "__main__":
    main()