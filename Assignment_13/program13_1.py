#===========================================================================
#
#   Problem Statement   :   Program to print area of a rectangle
#   Author              :   Ankur Takale
#
#===========================================================================

#===========================================================================
#
#   Function name   :   Area()
#   Description     :   Calculates area of rectangle
#   Input           :   length & width of rectangle
#   Output          :   Area of rectangle
#
#===========================================================================

def Area(length,width):
    area = length * width
    return area

#===========================================================================
#
#   Function name   :   main()
#   Description     :   Entry point function
#
#===========================================================================

def main():
    length = float(input("Enter length : "))
    width = float(input("Enter width : "))

    Ret = Area(length,width)

    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()