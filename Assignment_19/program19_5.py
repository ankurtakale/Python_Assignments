#===================================================================================================
#
#   Problem Statement   :   Write a program which contains filter(), map() and reduce() in it. Python 
#                           application which contains one list of numbers. List contains the numbers 
#                           which are accepted from user. Filter should filter out all prime numbers. 
#                           Map function will multiply each number by 2. Reduce will return Maximum number 
#                           from that numbers. (You can also use normal functions instead of lambda functions).
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

from functools import reduce

def Filter(no):

    for i in range(2,(no//2)+1):
        if (no % i) == 0:
            return False
        
    return True

def Map(no):

    return no * 2
    
def Reduce(no1,no2):
    
    if no1 > no2:
        return no1
    else:
        return no2

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