class Library:
    def __init__(self):
        self.books = {
            "The Great Gatsby": True,
            "1984": True,
            "To Kill a Mockingbird": True,
            "Pride and Prejudice": True,
            "The Catcher in the Rye": True,
            "Meditations": True,
            "The 48 Laws of Power": True,
            "The Courage to be Disliked": True
        }


    def display_books(self):
        print("Available books:")
        for book, available in self.books.items():
            if available:
                print(f"- {book}")


    def search_book(self):
        book_name = input("Enter the name of the book you want to search: ")
        if book_name in self.books:
            if self.books[book_name]:
                print(f"'{book_name}' is available.")
            else:
                print(f"'{book_name}' is currently not available.")
        else:
            print(f"'{book_name}' is not in the library.")


    def borrow_book(self):
        book_name = input("Enter the name of the book you want to borrow: ")
        if book_name in self.books:
            if self.books[book_name]:
                self.books[book_name] = False
                print(f"You have borrowed '{book_name}'.")
            else:
                print(f"'{book_name}' is currently not available.")
        else:
            print(f"'{book_name}' is not in the library.")


    def return_book(self):
        book_name = input("Enter the name of the book you want to return: ")
        if book_name in self.books:
            self.books[book_name] = True
            print(f"'{book_name}' has been returned.")
        else:
            print(f"'{book_name}' is not in the library.")
            choice = input(("Do you want to add this book to the library?   "))
            if choice=="Yes" or choice =='yes' or choice == 1:
                print("\n\n")
                library.add_book()
            else:
                print("Action closed")


    def add_book(self):
        book_name = input("Enter the name of the book: ")
        if book_name not in self.books:
            self.books[book_name] = True
            print(f"{book_name} is added to library!")
        else:
            print(f"{book_name} is already in the library.")        
library = Library()



while True:
    print("\n1.  Display available books")
    print("\n2.  Search for a book")
    print("\n3.  Borrow a book")
    print("\n4.  Return a book")
    print("\n5.  Add a book")
    print("\n6.  Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        print("\n\n")
        library.display_books()

    elif choice == '2':
        print("\n\n")
        library.search_book()

    elif choice == '3':
        print("\n\n")
        library.borrow_book()

    elif choice == '4':
        print("\n\n")
        library.return_book()

    elif choice =='5':
        print("\n\n")
        library.add_book()

    elif choice == '6':
        print("\n\nThank you for using my program!\n\n")
        break

    else:
        print("\n\n")
        print("Invalid choice. Please try again.")


