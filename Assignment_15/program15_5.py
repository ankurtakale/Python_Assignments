#===========================================================================
#
#   Problem Statement   :   Program which returns maximum of numbers in list 
#                           using reduce and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Maximum = lambda Max, no : Max if Max > no else no

def reduceX(Maximum,List):

    Max = List[0]

    for i in List:
        Max = Maximum(Max,i)

    return Max


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before reduce : ",List)

    Ret = reduceX(Maximum,List)

    print("Maximum is : ",Ret)
        

if __name__ == "__main__":
    main()