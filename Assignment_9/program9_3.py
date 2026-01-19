def Square(No):
    sqrt = No ** 2

    return sqrt

def main():
    Value = int(input("Enter number : "))
    
    Ret = Square(Value)

    print("Square is : ",Ret)

if __name__ == "__main__":
    main()