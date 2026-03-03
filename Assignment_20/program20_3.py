#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two threads named EvenList and OddList.
#                           Both threads should accept a list of integers as input. 
#                           The EvenList thread should:Extract all even elements from the list.
#                           Calculate and display their sum.The OddList thread should:Extract all odd elements from the list.
#                           Calculate and display their sum. Threads should run concurrently.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def Even(Data):

    Sum = 0
    elements = []

    for i in Data:
        if(i % 2) == 0:
            elements.append(i)
            Sum = Sum + i

    print("Even elements : ",elements)
    print("Sum of even elements : ",Sum)

def Odd(Data):

    Sum = 0
    elements = []

    for i in Data:
        if(i % 2) != 0:
            elements.append(i)
            Sum = Sum + i

    print("Odd elements : ",elements)
    print("Sum of odd elements : ",Sum)

def main():

    Data = []

    No = int(input("Enter number of elements in list : "))

    for i in range(No):
        value = int(input(f"Enter number{i+1} : "))
        Data.append(value)

    EvenList = threading.Thread(target=Even,args=(Data,))
    OddList = threading.Thread(target=Odd,args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join() 

if __name__ == "__main__":
    main()