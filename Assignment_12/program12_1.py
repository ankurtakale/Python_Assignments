def ChkVowel(ch):
    if(ch == 'a'or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        return True
    else:
        return False

def main():
    ch = input("Enter a character : ")

    Ret = ChkVowel(ch)

    if Ret == True:
        print("It is a vowel")
    else:
        print("It is a consonant")

if __name__ == "__main__":
    main()