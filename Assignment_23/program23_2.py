#=======================================================================================================================
#
#   Problem Statement   :   Write a Python program to implement a class named BankAccount with the following requirements:
#                           The class should contain two instance variables:Name (Account holder name)Amount (Account balance)
#                           The class should contain one class variable:ROI (Rate of Interest), initialized to 10.5
#                           Define a constructor (__init__) that accepts Name and initial Amount.
#                           Implement the following instance methods:
#                           Display() - displays account holder name and current balance 
#                           Deposit() - accepts an amount from the user and adds it to balance
#                           Withdraw() - accepts an amount from the user and subtracts it from balance
#                           (Ensure withdrawal is allowed only if sufficient balance exists)
#                           CalculateInterest() - calculates and returns interest using formula:
#                           Interest = (Amount * ROI) / 100
#                           Create multiple objects and demonstrate all methods.
#
#   Author              :   Ankur Takale
#
#=======================================================================================================================

class BankAccount:

    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account holder name : ",self.Name)
        print("Current balance : ",self.Amount)

    def Deposit(self,deposit):
        self.Amount = self.Amount + deposit

    def Withdraw(self,withdraw):
        if withdraw <= self.Amount:
            self.Amount = self.Amount - withdraw
        else:
            print("Insufficient balance")
            return
    
    def CalculateInterest(self):
        return(self.Amount * BankAccount.ROI) / 100

def main():

    obj1 = BankAccount("Ram",67000)
    obj1.Display()
    obj1.Deposit(34000)
    obj1.Display()
    obj1.Withdraw(23000)
    obj1.Display()
    print("Interest : ",obj1.CalculateInterest())

    obj2 = BankAccount("Virat",23000)
    obj2.Display()
    obj2.Deposit(3000)
    obj2.Display()
    obj2.Withdraw(40000)
    obj2.Display()
    print("Interest : ",obj2.CalculateInterest())

if __name__ == "__main__":
    main()