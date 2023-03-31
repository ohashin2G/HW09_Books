## Task 4

from books import books

# Create instances, adding a book
test_object = books.BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

test_object.add_book("War of the Worlds",4)

print('Number of books read:', test_object.num_books_read())