import unittest
from booklover import BookLover
import pandas as pd

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        """Test adding a book and checking if it appears in book_list."""
        bl = BookLover("Haejin Son", "umw7eg@virginia.edu", "romance")
        bl.add_book("Notebook", 4)
        self.assertTrue("Notebook" in bl.book_list['book_name'].values)

    def test_2_add_book(self):
        """Test adding the same book twice and ensure it's only in book_list once."""
        bl = BookLover("Grace Kelly", "gkelly@virginia.edu", "history")
        bl.add_book("Cold War", 5)
        bl.add_book("Cold War", 5)  # Adding duplicate
        self.assertEqual(len(bl.book_list[bl.book_list['book_name'] == "Cold War"]), 1)

    def test_3_has_read(self):
        """Test if a book in the list returns True for has_read()."""
        bl = BookLover("Sean Lee", "slee@virginia.edu", "classic")
        bl.add_book("Jane Eyre", 4)
        self.assertTrue(bl.has_read("Jane Eyre"))

    def test_4_has_read(self):
        """Test if a book NOT in the list returns False for has_read()."""
        bl = BookLover("Andrew Johnson", "ajohnson@virginia.edu", "sci-fi")
        self.assertFalse(bl.has_read("Dune"))  

    def test_5_num_books_read(self):
        """Test if num_books_read() returns the correct count after adding books."""
        bl = BookLover("Steven Johnson", "sjohnson@virginia.edu", "classic")
        bl.add_book("Romeo and Juliet", 3)
        bl.add_book("To Kill a Mockingbird", 5)
        bl.add_book("Great Gatsby", 4)
        self.assertEqual(bl.num_books_read(), 3)

    def test_6_fav_books(self):
        """Test if fav_books() only returns books with rating > 3."""
        bl = BookLover("Francisco Lee", "flee@virginia.edu", "religion")
        bl.add_book("Bible", 5)
        bl.add_book("Quran", 4)
        bl.add_book("Torah", 3) 
        
        fav_books = bl.fav_books()
        
        # Ensure all returned books have rating > 3
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main()