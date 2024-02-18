def add_book(books):
    bid = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    status = '0'  # available
    books.append((bid, title, author, status))
    print("Book added successfully!")
