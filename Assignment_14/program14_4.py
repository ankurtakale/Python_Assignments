#===========================================================================
#
#   Problem Statement   :   Program to print minimum number using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Min = lambda no1, no2 : min(no1,no2)
            
def main():
    Value1 = float(input("Enter number1 : "))
    Value2 = float(input("Enter number2 : "))

    Ret = Min(Value1, Value2)

    print("Minimum : ",Ret)

if __name__ == "__main__":
    main()