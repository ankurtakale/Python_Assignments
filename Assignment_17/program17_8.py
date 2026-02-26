#===================================================================================================
#
#   Problem Statement   :   Write a program which accepts a number and displays pattern
#                           1    
#                           1   2    
#                           1   2   3    
#                           1   2   3   4     
#                           1   2   3   4   5  
#                              
#   Author              :   Ankur Takale
#
#===================================================================================================

def Display(No):

    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end="  ")
        print()

def main():

    No = int(input("Enter number : "))

    Display(No)

if __name__ == "__main__":
    main()