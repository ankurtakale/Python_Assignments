#===========================================================================
#
#   Problem Statement   :   Program which returns list of strings having length
#                           greater than 5 using filter and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Check = lambda str : len(str) > 5 

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
        Value = str(input("Enter string : "))
        List.append(Value)

    print("Data before filter : ",List)

    Ret = filterX(Check,List)

    print("\nStrings having length greater than 5 are : \n")
    print("Data after filter : ",Ret)
        

if __name__ == "__main__":
    main()