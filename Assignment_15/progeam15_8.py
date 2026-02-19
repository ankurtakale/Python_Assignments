#===========================================================================
#
#   Problem Statement   :   Program which returns numbers divisible by 3 and 5
#                           using filter and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Check = lambda no : (no % 3) == 0 and (no % 5) == 0

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

    Ret = filterX(Check,List)

    print("Numbers divisible by 3 and 5 are : ",Ret)
        

if __name__ == "__main__":
    main()