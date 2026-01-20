def Display(No):
    for i in range(1,No+1):
        print(i,end="  ")
    
def main():
    Value1 = int(input("Enter a number : "))

    Ret = Display(Value1)

if __name__ == "__main__":
    main()