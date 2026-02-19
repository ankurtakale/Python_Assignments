#===========================================================================
#
#   Problem Statement   :   Program which returns count of even numbers using
#                           filter and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Count = lambda no : (no % 2) == 0

def filterX(Count,List):

    Result = 0

    for i in List:
        Ret = Count(i)
        if Ret == True:
            Result = Result + 1

    return Result


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before filter : ",List)

    Ret = filterX(Count,List)

    print("Count of even numbers is : ",Ret)
        

if __name__ == "__main__":
    main()