#===========================================================================
#
#   Problem Statement   :   Program which displays first 10 even numbers on screen
#   Author              :   Ankur Takale
#
#===========================================================================

def Display(No):

    for i in range(2,(No*2) + 1):
        if (i % 2) == 0:
            print(i,end="\t")
             
def main():

    Display(10)

if __name__ == "__main__":
    main()