#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates two threads named Prime and NonPrime.
#                           Both threads should accept a list of integers.
#                           The Prime thread should display all prime numbers from the list.
#                           The NonPrime thread should display all non-prime numbers from the list.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def displaynonprime(arr,nonprime_list):

    for no in arr:
        flag = False

        for i in range(2,(no//2)+1):
            if(no % i) == 0:
                flag = True
                break

        if flag:
            nonprime_list.append(no)

def displayprime(arr,prime_list):

    for no in arr:
        flag = True

        for i in range(2,(no//2)+1):
            if(no % i) == 0:
                flag = False
                break

        if flag:
            prime_list.append(no)

def main():

    value = int(input("Enter number of elements in list : "))

    values = list()
    prime_list = []
    nonprime_list = []

    for i in range(value):
        no = int(input(f"Enter element {i+1} : "))
        values.append(no)

    Prime = threading.Thread(target=displayprime,args=(values,prime_list))
    NonPrime = threading.Thread(target=displaynonprime,args=(values,nonprime_list))

    Prime.start()
    NonPrime.start()
    
    Prime.join()
    NonPrime.join()

    print("Prime List : ",prime_list)
    print("NonPrime List : ",nonprime_list)

if __name__ == "__main__":
    main()