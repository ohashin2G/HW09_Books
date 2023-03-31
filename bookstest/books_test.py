# %% [markdown]
# ## Task 2

# %%
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`
        
        #Create instances, adding a book
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
        booklv.add_book('War of the Worlds', 4)
        print(booklv.book_list)
        self.assertTrue(booklv.book_list['book_name'].eq('War of the Worlds').any())
       

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
        #booklv.has_read("test")
        booklv.add_book('Fight Club', 3)
        booklv.add_book('Fight Club', 3)
        print('num in the list is ', len(booklv.book_list))

        #Test if it is in 'book_list' only once
        #self.assertTrue(booklv, print)
        self.assertEqual(len(booklv.book_list), 1)
        #self.assertEqual(book_list[0]., book1)


    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
        booklv.add_book('Fight Club', 3)
                
        #Test if the answer is 'True'
        self.assertTrue(booklv.has_read('Fight Club'))



    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
        #booklv.add_book('Fight Club', 3)
             
        #Test if the answer is 'True'
        self.assertFalse(booklv.has_read('Fight Club2'))


    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')
        booklv.add_book("Forrest Gump", 4)
        booklv.add_book("Jurassic Park", 3)
        booklv.add_book("The Da Vinci Code", 4)

        #object1 = BookLover(name="new books")
        #for booklv in booklv.book_list:
        #  booklv.book_list.add_book(booklv)

        #booklv.has_read()

        #book3.has_read()
        #book4.has_read()
        #book5.has_read()

        #Test num_books matches expected
        self.assertEqual(booklv.num_books, 3)
        print(' test 5 - number of books: ',  booklv.num_books)


    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        booklv = BookLover('Han Solo', 'hsolo@millenniumfalcon.com', 'scifi')

        # Add some books with ratings to the list
        booklv.add_book("Forrest Gump", 4)
        booklv.add_book("Jurassic Park", 3)
        booklv.add_book("The Da Vinci Code", 2)
        booklv.add_book("Kitchen Confidential", 5)
        booklv.add_book("Murder on the Orient Express", 5)
        booklv.add_book("1Q84Murder on the Orient Express", 5)


        #Test if the favorite books have rating > 3
        fav_books = booklv.fav_books()
        self.assertGreater(len(fav_books), 3)
        print(' test 6 - number of rating > 3: ',  len(fav_books))
 

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



