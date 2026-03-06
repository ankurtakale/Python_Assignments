#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two threads.
#                           Thread 1 should calculate and display the maximum element from an list.
#                           Thread 2 should calculate and display the minimum element from the same list.
#                           The list should be accepted from the user.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def maximum(arr):

    Max = arr[0]

    for no in arr:
        if no > Max:
            Max = no

    print("Maximum element fro list is : ",Max)

def minimum(arr):

    Min = arr[0]

    for no in arr:
        if no < Min:
            Min = no

    print("Minimum element fro list is : ",Min)

def main():

    value = int(input("Enter number of elements in list : "))

    values = list()

    for i in range(value):
        no = int(input(f"Enter element {i+1} : "))
        values.append(no)

    t1 = threading.Thread(target=maximum,args=(values,))
    t2 = threading.Thread(target=minimum,args=(values,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()