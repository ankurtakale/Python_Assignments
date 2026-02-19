#===========================================================================
#
#   Problem Statement   :   Program to print square of each number in list using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Square = lambda no : no * no

def mapX(Square,List):
    Result = []

    for i in List:
        Ret = Square(i)

        Result.append(Ret)

    return Result


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before map : ",List)

    Ret = list(mapX(Square,List))

    print("Data after map : ",Ret)
        

if __name__ == "__main__":
    main()