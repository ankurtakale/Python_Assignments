#===================================================================================================
#
#   Problem Statement   :   Design a Python application where multiple threads update a shared variable.
#                           Use a Lock to avoid race conditions.
#                           Each thread should increment the shared counter multiple times.
#                           Display the final value of the counter after all threads complete execution.
#                                             
#   Author              :   Ankur Takale
#
#===================================================================================================

import threading

lobj = threading.Lock()

No = 1

def update():

    global No

    for i in range(5000):
        with lobj:
            No += 1

def main():

    t1 = threading.Thread(target=update)
    t2 = threading.Thread(target=update)
    t3 = threading.Thread(target=update)
    t4 = threading.Thread(target=update)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Final value of counter : ",No)

if __name__ == "__main__":
    main()