def Operations(No1,No2):
    add = No1 + No2
    sub = No1 - No2
    mul = No1 * No2
    if No2 == 0:
        div = None
    else:
        div = No1 / No2
    
    return add,sub,mul,div
    
def main():
    Value1 = int(input("Enter a number : "))
    Value2 = int(input("Enter a number : "))

    Ret = Operations(Value1,Value2)

    print("Addition is : ",Ret[0])
    print("Subtraction is : ",Ret[1])
    print("Multiplication is : ",Ret[2])

    if Ret[3] == None:
        print("Cannot divide by 0")
    else:
        print("Division is : ",Ret[3])

if __name__ == "__main__":
    main()