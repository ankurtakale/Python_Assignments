#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number and displays pattern
#                           *   *   *   *
#                           *   *   *   
#                           *   *  
#                           *   
#   Author              :   Ankur Takale
#
#===================================================================================================

def Display(No):

    for i in range(No,0,-1):
        for j in range(i):
            print("*",end="  ")
        print()

def main():

    No = int(input("Enter number : "))

    Display(No)

if __name__ == "__main__":
    main()