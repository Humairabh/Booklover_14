import numpy as np
import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book_lover = BookLover("Name", "Email", "Genre")
        book_lover.add_book("BookName", 4)
        self.assertTrue("BookName" in list(book_lover.book_list["book_name"]))
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book_lover_2 = BookLover("Name2", "Email2", "Genre2")
        book_lover_2.add_book("BookName", 3)
        book_lover_2.add_book("BookName", 3)
        self.assertEqual(list(book_lover_2.book_list["book_name"]).count("BookName"), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book_lover_3 = BookLover("Name3", "Email3", "Genre3")
        book_lover_3.add_book("BookName", 3)
        self.assertTrue(book_lover_3.has_read("BookName"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book_lover_4 = BookLover("Name4", "Email4", "Genre4")
        self.assertFalse(book_lover_4.has_read("BookName"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book_lover_5 = BookLover("Name5", "Email5", "Genre5")
        book_lover_5.add_book("BookName", 3)
        book_lover_5.add_book("BookName1", 4)
        book_lover_5.add_book("BookName2", 5)
        expected = book_lover_5.book_list.shape[0]
        actual = book_lover_5.num_books_read()
        self.assertEqual(expected, actual)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book_lover_6 = BookLover("Name6", "Email6", "Genre6")
        book_lover_6.add_book("BookName1", 1)
        book_lover_6.add_book("BookName2", 2) 
        book_lover_6.add_book("BookName3", 3)
        book_lover_6.add_book("BookName4", 4)
        book_lover_6.add_book("BookName5", 5)
        self.assertTrue(all([i>=3 for i in book_lover_6.fav_books()["book_rating"].values]))
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
