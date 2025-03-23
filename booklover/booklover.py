import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        """Parameters:
        name (str, required): The name of the person.
        email (str, required): The person's email, serving as a unique identifier.
        fav_genre (str, required): The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction).
        num_books (int, optional): Number of the books the person has read (default is 0).
        book_list (pd.DataFrame, optional): DataFrame with columns ['book_name', 'book_rating'].
        
        'book_name' is the title of the book the person has read.
        'book_rating' is the person’s rating of that book on a scale of 1 to 5, 
        where 1 means the person did not like the book at all, and 5 means the person loved the book.
        """
        self.name = name  
        self.email = email  
        self.fav_genre = fav_genre  
        self.num_books = num_books  
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name, rating):
        """
        Method 1. 
        Aadds a book to the list if it’s not already present.

        Parameters:
        book_name (str): The title of the book.
        rating (int): The rating of the book (1 to 5).
        """
        if not (0 <= rating <= 5):
            return "Error: rating should be an integer between 0 and 5."
    
        if book_name in self.book_list['book_name'].tolist():
            print(f"{book_name} is already in the book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books = len(self.book_list)  # Update the count of books read

    def has_read(self, book_name):
        """
        Method 2. 
        Checks if a book is in the list.
                
        Parameters:
        book_name (str): The title of the book.
        
        Returns:
        bool: True if the book exists, otherwise False.
        """
        return book_name in self.book_list['book_name'].tolist()

    def num_books_read(self):
        """Method 3. 
        Returns the total number of books read.
        
        Returns:
        int: Total count of books read.
        """
        return len(self.book_list)

    def fav_books(self):
        """Method 4. 
        Returns books rated greater than 3.
        
        Returns:
        pd.DataFrame: DataFrame containing books with rating > 3.
        """
        return self.book_list[self.book_list['book_rating'] > 3]
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")

    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 5)
    
    # Checking if a book was read
    print("Has read 'War of the Worlds'?", test_object.has_read("War of the Worlds"))  # Expected: True
    print("Has read 'Dune'?", test_object.has_read("Dune"))  # Expected: False

    # Checking number of books read
    print("Number of books read:", test_object.num_books_read())  # Expected: 5

    # Checking favorite books (rating > 3)
    print("Favorite books:\n", test_object.fav_books()) # Expected: 4


        
