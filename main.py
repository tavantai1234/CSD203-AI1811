from AddBook import add_book
from ViewBooks import view_books
from DeleteBook import delete_book
from BorrowedBook import borrow_book
from ReturnBook import return_book

def display_menu():
    print("Welcome to Library Management System")
    print("1. Add a Book")
    print("2. View Books")
    print("3. Delete a Book")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Exit")

def main():
    books = []
    borrowed_books = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            borrow_book(books, borrowed_books)
        elif choice == '5':
            return_book(books, borrowed_books)
        elif choice == '6':
            print("Thank you for using Library Management System")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
