#=======================================================================================================================
#
#   Problem Statement   :   Write a Python program to implement a class named Numbers with the following specifications:
#                           The class should contain one instance variable : Value
#                           Define a constructor (__init__) that accepts a number from the user and initializes Value. 
#                           Implement the following instance methods:
#                           ChkPrime() - returns True if the number is prime, otherwise returns False
#                           ChkPerfect() -returns True if the number is perfect, otherwise returns False
#                           Factors() -displays all factors of the number
#                           SumFactors() - returns the sum of all factors
#                           (You may use this method as a helper in ChkPerfect() if required)
#                           Create multiple objects and call all methods.
#
#   Author              :   Ankur Takale
#
#=======================================================================================================================

class Numbers:

    def __init__(self,value):
        self.Value = value

    def ChkPrime(self):
        for i in range(2,(self.Value // 2)+1):
            if(self.Value % i) == 0:
                return False
            
        return True
    
    def Factors(self):
        for i in range(1,(self.Value)+1):
            if(self.Value % i) == 0:
                print(i,end="  ")

    def SumFactors(self):
        sumfactor = 0

        for i in range(1,(self.Value // 2)+1):
            if(self.Value % i) == 0:
                sumfactor += i

        return sumfactor
    
    def ChkPerfect(self):
        return self.SumFactors() == self.Value

def main():

    obj1 = Numbers(25)
    print("Prime : ",obj1.ChkPrime())
    obj1.Factors()
    print("\nSum of factors : ",obj1.SumFactors())
    print("Perfect : ",obj1.ChkPerfect())

    obj2 = Numbers(17)
    print("Prime : ",obj2.ChkPrime())
    obj2.Factors()
    print("\nSum of factors : ",obj2.SumFactors())
    print("Perfect : ",obj2.ChkPerfect())

if __name__ == "__main__":
    main()