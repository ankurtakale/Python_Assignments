def ChkPrime(No):
    if No < 2:
        return False
    for i in range(2,int(No/2)+1):
        if(No % i) == 0:
            return False
    return True

def main():
    Value = int(input("Enter number : "))

    Ret = ChkPrime(Value)

    if Ret == True:
        print(Value,"is a prime number")
    else:
        print(Value,"is not a prime number")

if __name__ == "__main__":
    main()