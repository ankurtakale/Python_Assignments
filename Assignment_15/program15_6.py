#===========================================================================
#
#   Problem Statement   :   Program which returns minimum of numbers in list 
#                           using reduce and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Minimum = lambda Min, no : Min if Min < no else no

def reduceX(Minimum,List):

    Min = List[0]

    for i in List:
        Min = Minimum(Min,i)

    return Min


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before reduce : ",List)

    Ret = reduceX(Minimum,List)

    print("Minimum is : ",Ret)
        

if __name__ == "__main__":
    main()