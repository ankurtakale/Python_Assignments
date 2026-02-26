#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number and returns number of digits in that number
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Display(No):

    Count = 0

    if No == 0:
        return 1
    
    if No < 0:
        No = -No

    while(No > 0):
        No = No // 10
        Count += 1

    return Count

def main():

    No = int(input("Enter number : "))

    Ret = Display(No)

    print(f"Number of digits in {No} are : {Ret}")

if __name__ == "__main__":
    main()