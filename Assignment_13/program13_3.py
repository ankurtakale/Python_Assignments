#===========================================================================
#
#   Problem Statement   :   Program to check if number is perfect or not
#   Author              :   Ankur Takale
#
#===========================================================================

#===========================================================================
#
#   Function name   :   ChkPerfect()
#   Description     :   Checks the sum of factors is equal to that number or not
#   Input           :   Number
#   Output          :   Returns boolean value like True of False
#
#===========================================================================

def ChkPerfect(no):
    sum = 0

    for i in range(1,(no//2)+1):
        if(no % i == 0):
            sum = sum + i

    print(sum == no)
    return (sum == no)

#===========================================================================
#
#   Function name   :   main()
#   Description     :   Entry point function
#
#===========================================================================

def main():
    Value = int(input("Enter number : "))

    Ret = ChkPerfect(Value)

    if(Ret == True):
        print(Value,"is a perfect number")
    else:
        print(Value,"is not a perfect number")

if __name__ == "__main__":
    main()