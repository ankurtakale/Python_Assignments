#=======================================================================================================================
#
#   Problem Statement   :   Write a Python program to implement a class named BookStore with the following specifications:
#                           The class should contain two instance variables:Name (Book Name)Author (Book Author)
#                           The class should contain one class variable:NoOfBooks (initialize it to 0)
#                           Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
#                           (Inside the constructor, increment the class variable NoOfBooks by 1 
#                           whenever a new object iscreated.
#                           Implement an instance method:Display() - should display book details in the 
#                           format:<BookName> by <Author>. No of books: <NoOfBooks>

#   Author              :   Ankur Takale
#
#=======================================================================================================================

class BookStore:

    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books : {BookStore.NoOfBooks}")

def main():

    obj1 = BookStore("C Programming","Dennis Ritchie")
    obj1.Display()

    obj2 = BookStore("Linux Programming Interface","Michael Kerrisk")
    obj2.Display()

if __name__ == "__main__":
    main()