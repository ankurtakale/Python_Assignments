#===========================================================================
#
#   Problem Statement   :   Program which returns multiplication of two numbers using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Multiplication = lambda no1, no2: no1 * no2
            
def main():
    Value1 = float(input("Enter number1 : "))
    Value2 = float(input("Enter number2 : "))

    Ret = Multiplication(Value1, Value2)

    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()