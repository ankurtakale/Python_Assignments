#===========================================================================
#
#   Problem Statement   :   Program which returns maximum of three numbers using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Maximum = lambda no1, no2, no3: max(no1 ,no2, no3)
            
def main():
    Value1 = float(input("Enter number1 : "))
    Value2 = float(input("Enter number2 : "))
    Value3 = float(input("Enter number3 : "))

    Ret = Maximum(Value1, Value2, Value3)

    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()