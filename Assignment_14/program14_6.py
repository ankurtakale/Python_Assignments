#===========================================================================
#
#   Problem Statement   :   Program which returns True if number is Odd otherwise 
#                           returns False for Even using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Check = lambda no: (no % 2 != 0)
            
def main():
    Value = float(input("Enter number : "))

    Ret = Check(Value)

    print(Ret)

if __name__ == "__main__":
    main()