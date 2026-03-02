#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a list also a number and returns frequency 
#                           of that number from that list
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Frequency(List,no):

    Count = 0

    for i in range(len(List)):
        if List[i] == no:
            Count += 1

    return Count

def main():

    List = []

    No = int(input("Enter number of elements : "))

    for i in range(1,No+1):
        value = int(input(f"Enter element {i} : "))
        List.append(value)

    search_no = int(input("\nEnter element to search : "))

    Ret = Frequency(List,search_no)

    print(f"\nFrequency of element from list is : {Ret}")

if __name__ == "__main__":
    main()