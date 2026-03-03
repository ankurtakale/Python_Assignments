#===================================================================================================
#
#   Problem Statement   :   Design a Python application that creates three threads named Small, Capital, and Digits.
#                           All threads should accept a string as input.
#                           The Small thread should count and display the number of lowercase characters.
#                           The Capital thread should count and display the number of uppercase characters.
#                           The Digits thread should count and display the number of numeric digits.
#                           Each thread must also display:
#                           Thread ID 
#                           Thread Name
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

def small(str):

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Count = 0
    elements = []

    for i in str:
        if(i >= 'a') and (i <= 'z'):
            Count += 1
            elements.append(i)

    print("Lowercase characters : ",elements)
    print("Count of lowercase characters : ",Count)
    print("-"*80)

def capital(str):

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Count = 0
    elements = []

    for i in str:
        if(i >= 'A') and (i <= 'Z'):
            Count += 1
            elements.append(i)

    print("Uppercase characters : ",elements)
    print("Count of uppercase characters : ",Count)
    print("-"*80)

def digit(str):

    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

    Count = 0
    elements = []

    for i in str:
        if(i >= '0') and (i <= '9'):
            Count += 1
            elements.append(i)

    print("Digits : ",elements)
    print("Count of digits : ",Count)

def main():

    str = input("Enter string : ")

    Small = threading.Thread(target=small,args=(str,))
    Capital = threading.Thread(target=capital,args=(str,))
    Digits = threading.Thread(target=digit,args=(str,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join() 
    Digits.join()

if __name__ == "__main__":
    main()