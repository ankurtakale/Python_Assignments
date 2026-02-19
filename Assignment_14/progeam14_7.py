#===========================================================================
#
#   Problem Statement   :   Program which returns True if number is divisible 
#                           by 5 using lambda
#   Author              :   Ankur Takale
#
#===========================================================================

Check = lambda no: (no % 5 == 0)
            
def main():
    Value = float(input("Enter number : "))

    Ret = Check(Value)

    print(Ret)

if __name__ == "__main__":
    main()