from user_manage import LibraryManagementSystem as user
from Book_manage import Book
from rent_manage import Book_rent


def main():
    library_system = user()
    book_system=Book()
    Borrow_system=Book_rent()

    while True:
        print("\n=== Library Management System ===")
        print("1. Add New User")
        print("2. Display Users")
        print("3. Add book")
        print("4. Display book")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            library_system.add_user()
            
        elif choice == '2':
            library_system.display_users()

        elif choice == '3':
            book_system.add_book()
        elif choice == '4':
            book_system.display_book()
        elif choice == '5':
            Borrow_system.Book_borrows()
            
        elif choice == '6':
            Borrow_system.book_return()
            
        elif choice == '7':
            print("Exiting Library Management System. Goodbye!")
            
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
