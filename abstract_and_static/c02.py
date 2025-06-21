from abc import ABC, abstractmethod


class LibraryItem(ABC):
  '''Library Item class (an abstract class so inherits from ABC)'''

  @__________________
  def check_out(self) -> None:  # ABSTRACT METHOD
    pass

  @____________________
  def return_item(self) -> None:  # ABSTRACT METHOD
    pass

  def display_info(self) -> None:  # VIRTUAL METHOD
    print("Displaying information about the library item.")


class Book(______________):
  '''Book inherits from Library Item'''

  def _____________(self) -> None:  # Overriding
    print("Checking out the book.")

  def return_item(self) -> None:  # Overriding
    print("Returning the book.")

  def _____________(self) -> None:  # Overriding
    print("Displaying information about the book.")


class DVD(________________):
  '''DVD inherits from Library Item'''

  def check_out(self) -> None:  # Overriding
    print("Checking out the DVD.")

  def ______________(self) -> None:  # Overriding
    print("Returning the DVD.")

  def display_info(self) -> None:  # Overriding
    print("Displaying information about the DVD.")


book: Book = Book()  # create an instance of Book
book.____________()  # check out
book.____________()  # return item
book.display_info()  # display info

dvd: DVD = DVD()  # create an instance of DVD
dvd.check_out()  # check out
dvd.return_item()  # return item
dvd.______________()  # display info
