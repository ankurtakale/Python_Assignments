#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a list and returns addition of elements in that list
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Addition(List):

    Sum = 0

    for i in range(len(List)):
        Sum = Sum + List[i]

    return Sum

def main():

    List = []

    No = int(input("Enter number of elements : "))

    for i in range(1,No+1):
        value = int(input(f"Enter element {i} : "))
        List.append(value)

    Ret = Addition(List)

    print(f"Addition of all elements from list is : {Ret}")

if __name__ == "__main__":
    main()