#===========================================================================
#
#   Problem Statement   :   Program which returns addition of two numbers using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Addition = lambda no1, no2: no1 + no2
            
def main():
    Value1 = float(input("Enter number1 : "))
    Value2 = float(input("Enter number2 : "))

    Ret = Addition(Value1, Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()