#===========================================================================
#
#   Problem Statement   :   Program to print area of a circle
#   Author              :   Ankur Takale
#
#===========================================================================

#===========================================================================
#
#   Function name   :   Area()
#   Description     :   Calculates area of circle
#   Input           :   Radius of circle
#   Output          :   Area of circle
#
#===========================================================================

def Area(radius):
    area = 3.14 * radius * radius

    return area

#===========================================================================
#
#   Function name   :   main()
#   Description     :   Entry point function
#
#===========================================================================

def main():
    radius = int(input("Enter radius : "))

    Ret = Area(radius)

    print("Area of circle is : ",Ret)

if __name__ == "__main__":
    main()