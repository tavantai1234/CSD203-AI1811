def delete_book(books):
    bid = input("Enter book id to delete: ")
    for book in books:
        if book[0] == bid:
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Book with id {} not found.".format(bid))
