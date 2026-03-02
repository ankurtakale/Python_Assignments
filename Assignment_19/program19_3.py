#===================================================================================================
#
#   Problem Statement   :   Write a program which contains filter(), map() and reduce() in it. 
#                           Python application which contains one list of numbers. List contains the numbers 
#                           which are accepted from user. Filtershould filter out all such numbers which 
#                           greater than or equal to 70 and less than or equal to 90. Map function will 
#                           increase each number by 10. Reduce will return product of all that numbers.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

from functools import reduce

Filter = lambda no : no >= 70 and no <= 90

Map = lambda no : no + 10

Reduce = lambda a,no : a * no

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