#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two threads.
#                           Thread 1 should compute the sum of elements from a list.
#                           Thread 2 should compute the product of elements from the same list.
#                           Return the results to the main thread and display them.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def summation(arr,result):

    Sum = 0

    for no in arr:
        Sum += no
        
    result.append(Sum)

def product(arr,result):

    Mul = 1

    for no in arr:
        Mul *= no
        
    result.append(Mul)

def main():

    value = int(input("Enter number of elements in list : "))

    values = list()

    sum_res = []
    mul_res = []

    for i in range(value):
        no = int(input(f"Enter element {i+1} : "))
        values.append(no)

    t1 = threading.Thread(target=summation,args=(values,sum_res))
    t2 = threading.Thread(target=product,args=(values,mul_res))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Sum of elements from list : ",sum_res)
    print("Product of elements from list : ",mul_res)

if __name__ == "__main__":
    main()