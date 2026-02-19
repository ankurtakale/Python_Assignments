#===========================================================================
#
#   Problem Statement   :   Program to display grades based on marks
#   Author              :   Ankur Takale
#
#===========================================================================

def Print(no):
    
    if(no >= 75):
       print("Distinction")
    elif(no >= 60):
       print("First class")
    elif(no >= 50):
       print("Second class")
    else:
       print("Fail")

def main():
    Value = int(input("Enter marks : "))

    Print(Value)

if __name__ == "__main__":
    main()