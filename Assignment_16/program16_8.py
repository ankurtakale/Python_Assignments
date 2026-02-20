#===========================================================================
#
#   Problem Statement   :   Program which accepts a number from user and 
#                           prints that number of * on screen
#   Author              :   Ankur Takale
#
#===========================================================================

def Display(No):

    for i in range(No):
        print("*",end="\t")
             
def main():

    Value = int(input("Enter number : "))

    Display(Value)

if __name__ == "__main__":
    main()