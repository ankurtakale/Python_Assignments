#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number and returns addition of digits in that number
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Addition(No):

    Sum = 0

    if No == 0:
        return 1
    
    if No < 0:
        No = -No

    while(No > 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():

    No = int(input("Enter number : "))

    Ret = Addition(No)

    print(f"Addition of digits in {No} is : {Ret}")

if __name__ == "__main__":
    main()