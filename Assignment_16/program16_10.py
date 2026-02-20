#===========================================================================
#
#   Problem Statement   :   Program which accepts name from user and display 
#                           length of that name
#   Author              :   Ankur Takale
#
#===========================================================================

def Display(name):

    Count = 0

    for i in name:
        Count = Count + 1

    return Count
             
def main():

    name = input("Enter name : ")

    Ret = Display(name)

    print(f"Length : {Ret}")

if __name__ == "__main__":
    main()