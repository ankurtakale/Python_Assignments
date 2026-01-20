def ChkPalindrome(No):
    Digit = 0
    Temp = No
    Rev = 0

    if No < 0:
        No = -No

    while(No > 0):
        Digit = No % 10
        Rev = (Rev * 10) + Digit
        No = No // 10

    if Temp == Rev:
        return True
    else:
        return False

def main():
    Value = int(input("Enter number : "))

    Ret = ChkPalindrome(Value)   

    if Ret == True:
        print(Value,"is a palindrome")
    else:
        print(Value,"is not a palindrome")

if __name__ == "__main__":
    main()