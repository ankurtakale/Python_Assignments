#===========================================================================
#
#   Problem Statement   :   Program which returns true if it is divisible by 5 else false
#   Author              :   Ankur Takale
#
#===========================================================================

def Check(No):

    return No % 5 == 0
             
def main():

    Value = float(input("Enter number : "))

    Ret = Check(Value)

    print(Ret)

if __name__ == "__main__":
    main()