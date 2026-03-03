#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two threads named EvenFactor and OddFactor.
#                           Both threads should accept one integer number as a parameter.. 
#                           The EvenFactor thread should:Identify all even factors of the given number.
#                           Calculate and display the sum of even factors.
#                           The OddFactor thread should:Identify all odd factors of the given number.
#                           Calculate and display the sum of odd factors.After both threads complete execution, 
#                           the main thread should display the message:"Exit from main"
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def Even(No):

    Sum = 0
    factors = []

    for i in range(1,No+1):
        if(No % i) == 0 and (i % 2) == 0:
            factors.append(i)
            Sum = Sum + i

    print("Even factors : ",factors)
    print("Sum of even factors : ",Sum)

def Odd(No):

    Sum = 0
    factors = []

    for i in range(1,No+1):
        if(No % i) == 0 and (i % 2) != 0:
            factors.append(i)
            Sum = Sum + i

    print("Odd factors : ",factors)
    print("Sum of odd factors : ",Sum)

def main():

    No = int(input("Enter number : "))

    EvenFactor = threading.Thread(target=Even,args=(No,))
    OddFactor = threading.Thread(target=Odd,args=(No,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join() 

    print("Exit from main")

if __name__ == "__main__":
    main()