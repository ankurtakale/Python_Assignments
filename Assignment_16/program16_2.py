#===========================================================================
#
#   Problem Statement   :   Write a program which contains a function and it 
#                           checks whether the number is even or odd 
#   Author              :   Ankur Takale
#
#===========================================================================

def ChkNum(No):

    if (No % 2) == 0:
        print("Even number")
    else:
        print("Odd number")

def main():

    Value = int(input("Enter number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()