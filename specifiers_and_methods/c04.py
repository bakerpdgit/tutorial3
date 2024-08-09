from abc import ABC, abstractmethod

# Abstract base class
class LibraryItem(ABC):

    @__________________
    def check_out(self): # ABSTRACT METHOD
        pass

    @____________________
    def return_item(self): # ABSTRACT METHOD
        pass

    def display_info(self): # VIRTUAL METHOD
        print("Displaying information about the library item.")

    @____________________
    def get_library_name():
        return "My Library"

class Book(______________): # Book inherits from Library Item

    def _____________(self): # Overriding
        print("Checking out the book.")

    def return_item(self): # Overriding
        print("Returning the book.")

    def _____________(self): # Overriding
        print("Displaying information about the book.")

class DVD(________________): # DVD inherits from Library Item

    def check_out(self): # Overriding
        print("Checking out the DVD.")

    def ______________(self): # Overriding
        print("Returning the DVD.")

    def display_info(self): # Overriding
        print("Displaying information about the DVD.")



book = Book() # create an instance of Book
book.____________() # check out
book.____________() # return item
book.display_info() # display info
print(LibraryItem.get_library_name()) # get library name

dvd = DVD() # create an instance of DVD
dvd.check_out() # check out
dvd.return_item() # return item
dvd.______________() # display info
print(LibraryItem._____________________()) # get library name