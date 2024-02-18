def return_book(books, borrowed_books):
    bid = input("Enter book id to return: ")
    for book in books:
        if book[0] == bid:
            book_index = books.index(book)
            books[book_index] = (book[0], book[1], book[2], '0')  # mark as available
            for borrowed_book in borrowed_books:
                if borrowed_book[0] == bid:
                    borrowed_books.remove(borrowed_book)
                    print("Book returned successfully!")
                    return
            print("Book not found in borrowed list.")
            return
    print("Book with id {} not found.".format(bid))
