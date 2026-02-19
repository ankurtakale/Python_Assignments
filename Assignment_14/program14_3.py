#===========================================================================
#
#   Problem Statement   :   Program to print maximum number using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Max = lambda no1, no2 : max(no1,no2)
            
def main():
    Value1 = float(input("Enter number1 : "))
    Value2 = float(input("Enter number2 : "))

    Ret = Max(Value1, Value2)

    print("Maximum : ",Ret)

if __name__ == "__main__":
    main()