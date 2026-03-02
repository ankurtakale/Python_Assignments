#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts N numbers from user and store it into a list 
#                           returns addition of all prime numbers from that list. Main python file accepts 
#                           N numbers from user and pass each number to ChkPrime() function which is a part 
#                           of our user defined module named as Num. Name of the function from main python 
#                           file should be ListPrime().
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

from Num import ChkPrime

def ListPrime(List):
    Sum = 0

    for i in List:
        if ChkPrime(i):
            Sum = Sum + i

    return Sum
    
def main():

    List = []

    No = int(input("Enter number of elements : "))

    for i in range(1,No+1):
        value = int(input(f"Enter element {i} : "))
        List.append(value)

    Ret = ListPrime(List)

    print("Addition of prime numbers : ",Ret)

if __name__ == "__main__":
    main()