#===========================================================================
#
#   Problem Statement   :   Program to filter list of odd numbers in list using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Check = lambda no : (no % 2) != 0

def filterX(Check,List):
    Result = []

    for i in List:
        Ret = Check(i)
        if Ret == True:
            Result.append(i)

    return Result


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before filter : ",List)

    Ret = list(filterX(Check,List))

    print("Data after filter : ",Ret)
        

if __name__ == "__main__":
    main()