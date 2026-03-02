#===================================================================================================
#
#   Problem Statement   :   Write a program which contains one lambda function has two parameters and 
#                           return multiplication
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

mult = lambda no1,no2 : no1 * no2

def main():

    No1 = int(input("Enter number1 : "))
    No2 = int(input("Enter number2 : "))

    Ret = mult(No1,No2)

    print(Ret)

if __name__ == "__main__":
    main()