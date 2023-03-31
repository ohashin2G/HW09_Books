## Task 1

import pandas as pd
import numpy as np

class BookLover:

  book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

# constructor
  def __init__(self, name, email, fav_genre, num_books=0,book_list = pd.DataFrame({'book_name':[],'book_rating':[]})):
    self.name = name    
    self.email = email
    self.fav_genre = fav_genre
    self.num_books = num_books
    self.book_list = book_list
    #print('This is right BookLover file')


# Method 1
  def add_book(self, pass_book_name, book_rating):
    
    #if book_name in self.book_list['book_name']:
    if self.book_list['book_name'].eq(pass_book_name).any():
      print(f"{pass_book_name} is already in your book list")
    else:
      new_book2 = {'book_name':pass_book_name, 'book_rating':book_rating}
      self.book_list = self.book_list.append(new_book2,ignore_index=True)
      self.num_books += 1
      print(f"{pass_book_name} rated {book_rating} has been added")
    


# Method 2
  def has_read(self, passed_book_name):
    #print(' in has read - the passed book name is >>', passed_book_name, '<<' )
    #print(' self book list is' , self.book_list)
    #if self.book_list['book_name'].eq(passed_book_name).any():
    if self.book_list['book_name'].eq(passed_book_name).any():
      return True
    else:
      return False



 # Method 3
  def num_books_read(self):
      return self.num_books


# Method 4
  def fav_books(self):
    return self.book_list[self.book_list['book_rating'] >3]

if __name__ == '__main__':

  test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
  test_object.add_book("War of the Worlds",4)
  test_object.has_read("War of the Worlds")
  test_object.num_books_read()
  test_object.fav_books()