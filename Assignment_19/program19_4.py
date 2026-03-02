#===================================================================================================
#
#   Problem Statement   :   Write a program which contains filter(), map() and reduce() in it. Python 
#                           application which contains one list of numbers. List contains the numbers 
#                           which are accepted from user. Filter should filter out all such numbers which 
#                           are even. Map function will calculate its square. Reduce will return addition 
#                           of all that numbers.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

from functools import reduce

Filter = lambda no : (no % 2) == 0

Map = lambda no : no * no

Reduce = lambda a,no : a + no

def main():

    Data = []

    No = int(input("Enter number of elements in list : "))

    for i in range(No):
        Ret = int(input(f"Enter element {i+1} : "))
        Data.append(Ret)

    print("Original data : ",Data)

    Fdata = list(filter(Filter,Data))
    print("Data after filter : ",Fdata)

    Mdata = list(map(Map,Fdata))
    print("Data after map : ",Mdata)

    Rdata = (reduce(Reduce,Mdata))
    print("Data after reduce : ",Rdata)
    

if __name__ == "__main__":
    main()