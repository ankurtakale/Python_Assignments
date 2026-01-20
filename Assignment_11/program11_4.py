def RevNum(No):
    Digit = 0

    while(No > 0):
        Digit = No % 10
        print(Digit, end="")
        No = No // 10

def main():
    Value = int(input("Enter number : "))

    RevNum(Value)   

if __name__ == "__main__":
    main()