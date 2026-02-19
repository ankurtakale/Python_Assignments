#===========================================================================
#
#   Problem Statement   :   Program which returns product of numbers in list 
#                           using reduce and lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Product = lambda A, B : A * B

def reduceX(Product,List):

    Ret = 1

    for i in List:
        Ret = Product(Ret,i)

    return Ret


def main():

    List = []

    number = (int(input("Enter number of elements in list : ")))

    for i in range(number):
        Value = float(input("Enter element : "))
        List.append(Value)

    print("Data before reduce : ",List)

    Ret = reduceX(Product,List)

    print("Product is : ",Ret)
        

if __name__ == "__main__":
    main()