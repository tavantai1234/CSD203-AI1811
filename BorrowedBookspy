def borrow_book(books, borrowed_books):
    bid = input("Enter book id to borrow: ")
    for book in books:
        if book[0] == bid and book[3] == '0':  # available
            borrower = input("Enter borrower name: ")
            borrowed_books.append((bid, borrower))
            book_index = books.index(book)
            books[book_index] = (book[0], book[1], book[2], '1')  # mark as issued
            print("Book borrowed successfully!")
            return
    print("Book with id {} not available.".format(bid))
