#=======================================================================================================================
#
#   Problem Statement   :   Write a Python program to implement a class named Arithmetic with the following characteristics:
#                           The class should contain two instance variables: Value1 and Value2.
#                           Define a constructor (__init__) that initializes all instance variables to 0.
#                           Implement the following instance methods:
#                           Accept() - accepts values for Value1 and Value2 from the user.
#                           Addition() -returns the addition of Value1 and Value2.
#                           Subtraction() - returns the subtraction of Value1 and Value2.
#                           Multiplication() -returns the multiplication of Value1 and Value2.
#                           Division() - returns the division of Value1 and Value2 (handle division by zeroproperly).
#                           Create multiple objects of the Arithmetic class and invoke all the instance methods.
#                           
#   Author              :   Ankur Takale
#
#=======================================================================================================================

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter value1 : "))
        self.Value2 = float(input("Enter value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        try:
            return self.Value1 / self.Value2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
            return

def main():

    obj1 = Arithmetic()
    obj2 = Arithmetic()
    obj3 = Arithmetic()

    obj1.Accept()
    print("Addition is : ",obj1.Addition())
    print("Subtraction is : ",obj1.Subtraction())
    print("Multiplication is : ",obj1.Multiplication())
    print("Division is : ",obj1.Division())
    print("-"*70)

    obj2.Accept()
    print("Addition is : ",obj2.Addition())
    print("Subtraction is : ",obj2.Subtraction())
    print("Multiplication is : ",obj2.Multiplication())
    print("Division is : ",obj2.Division())
    print("-"*70)

    obj3.Accept()
    print("Addition is : ",obj3.Addition())
    print("Subtraction is : ",obj3.Subtraction())
    print("Multiplication is : ",obj3.Multiplication())
    print("Division is : ",obj3.Division())
    print("-"*70)

if __name__ == "__main__":
    main()