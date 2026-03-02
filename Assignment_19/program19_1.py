#===================================================================================================
#
#   Problem Statement   :   Write a program which contains one lambda function and return power of two
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

power = lambda no : 2 ** no

def main():

    No = int(input("Enter number : "))

    Ret = power(No)

    print(Ret)

if __name__ == "__main__":
    main()