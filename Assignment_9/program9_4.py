def Cube(No):
    cube = No ** 3

    return cube

def main():
    Value = int(input("Enter number : "))
    
    Ret = Cube(Value)

    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()