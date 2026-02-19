#===========================================================================
#
#   Problem Statement   :   Program which returns addition of numbers in list 
#                           using reduce and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Addition = lambda A, B : A + B

def reduceX(Addition,List):

    Sum = 0

    for i in List:
        Sum = Addition(Sum,i)

    return Sum


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before reduce : ",List)

    Ret = reduceX(Addition,List)

    print("Addition is : ",Ret)
        

if __name__ == "__main__":
    main()