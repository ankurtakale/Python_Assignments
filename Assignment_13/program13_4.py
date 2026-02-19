#===========================================================================
#
#   Problem Statement   :   Program to print binary equivalent of a number
#   Author              :   Ankur Takale
#
#===========================================================================

def Print(no):
    
    binary = bin(no)[2:]

    return binary

def main():
    Value = int(input("Enter number : "))

    Ret = Print(Value)

    print("Binary equivalent : ",Ret)

if __name__ == "__main__":
    main()