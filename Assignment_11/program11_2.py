def CountDigit(No):
    Count = 0

    while(No > 0):
        Count += 1
        No = No // 10

    return Count

def main():
    Value = int(input("Enter number : "))

    Ret = CountDigit(Value)

    print("Count of digit is : ",Ret)    

if __name__ == "__main__":
    main()