def SumDigit(No):
    Digit = 0
    Sum = 0

    while(No > 0):
        Digit = No % 10
        Sum += Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter number : "))

    Ret = SumDigit(Value)

    print("Sum of digit is : ",Ret)    

if __name__ == "__main__":
    main()