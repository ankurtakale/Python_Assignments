def ChkDivisible(No):
    if ((No % 3 == 0) and (No % 5 == 0)):
        print(No,"is divisible by 3 and 5")
    else:
        print(No,"is not divisible by 3 and 5")
   
def main():
    Value = int(input("Enter number : "))
    
    ChkDivisible(Value)

if __name__ == "__main__":
    main()