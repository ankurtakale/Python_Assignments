#===========================================================================
#
#   Problem Statement   :   Program to print cube of a number using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Cube = lambda no : no * no * no

def main():
    Value = float(input("Enter number : "))

    Ret = Cube(Value)

    print("Cube : ",Ret)

if __name__ == "__main__":
    main()