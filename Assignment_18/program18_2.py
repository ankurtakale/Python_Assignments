#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a list and returns maximum number from that list
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Maximum(List):

    Max = List[0]

    for i in range(len(List)):
        if Max < List[i]:
            Max = List[i]

    return Max

def main():

    List = []

    No = int(input("Enter number of elements : "))

    for i in range(1,No+1):
        value = int(input(f"Enter element {i} : "))
        List.append(value)

    Ret = Maximum(List)

    print(f"Maximum element from list is : {Ret}")

if __name__ == "__main__":
    main()