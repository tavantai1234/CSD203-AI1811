def view_books(books):
    if not books:
        print("No books available.")
    else:
        print("Bid | Title | Author | Status")
        print("-" * 30)
        for book in books:
            print(" | ".join(book))
