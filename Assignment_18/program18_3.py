#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a list and returns minimum number from that list
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Minimum(List):

    Min = List[0]

    for i in range(len(List)):
        if Min > List[i]:
            Min = List[i]

    return Min

def main():

    List = []

    No = int(input("Enter number of elements : "))

    for i in range(1,No+1):
        value = int(input(f"Enter element {i} : "))
        List.append(value)

    Ret = Minimum(List)

    print(f"Minimum element from list is : {Ret}")

if __name__ == "__main__":
    main()