#===========================================================================
#
#   Problem Statement   :   Program which checks whether number is positive, 
#                           negative or zero
#   Author              :   Ankur Takale
#
#===========================================================================

def Check(No):

    if No > 0:
        print("Positive number")
    elif No < 0:
        print("Negative number")
    elif No == 0:
        print("Zero")

def main():

    Value = float(input("Enter number : "))

    Check(Value)

if __name__ == "__main__":
    main()