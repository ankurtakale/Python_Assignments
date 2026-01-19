def Sum(No):
    sum = 0
    for i in range(1,No+1):
        sum = sum + i
    
    return sum

def main():
    Value = int(input(("Enter a number : ")))
    
    Ret = Sum(Value)

    print(Ret)

if __name__ == "__main__":
    main()