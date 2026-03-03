#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two separate threads named Even and Odd.
#                           The Even thread should display the first 10 even numbers.
#                           The Odd thread should display the first 10 odd numbers.
#                           Both threads should execute independently using the threading module. 
#                           Ensure proper thread creation and execution.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def Even(No):

    for i in range(No*2):
        if(i % 2) == 0:
            print(i,end="  ")

    print()

def Odd(No):

    for i in range(No*2+1):
        if(i % 2) != 0:
            print(i,end="  ")

    print()

def main():

    even = threading.Thread(target=Even,args=(10,))
    odd = threading.Thread(target=Odd,args=(10,))

    even.start()
    odd.start()

    even.join()
    odd.join()

if __name__ == "__main__":
    main()