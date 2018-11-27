# Create a User
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = []

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.address = address
        return self.name + ', your email address has been updated to ' + str(self.address) +"."
        
    def __repr__(self):
        return "{}, {}".format(self.name, self.email)
        
    def __eq__(self, other):
        if isinstance(other, User):
          return (self.name == other.name) and (self.email == other.email)
        else:
          return False
    def __ne__(self, other):
        return (not self.__eq__(other))

    def read_book(self, book, rating=None):
        if rating is not None:
            self.books = {book: rating}
            #print(self.books)
            
    def get_average_rating(self):
        rating_scores = 0
        books_count = 0
        for book in self.books:
            if self.books[book] is not None:
                rating_scores += self.books[book]
                books_count += 1
                #print(self.name, rating_scores, books_count)
        if books_count == 0:
            print("This user hasn't rated any books.")
        else:
            average_rating = rating_scores / books_count 
            return average_rating

    
# Create a Book
class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.new_isbn = new_isbn
        return "The isbn of {} has been changed to {}. ".format(self.title, self.new_isbn)
    
    def __repr__(self):
        return "{} with isbn number {}".format(self.title, self.isbn)
    
    # a book objct should be equal to another book object if they both have the same title and isbn
    def __eq__(self, other):
        if isinstance(other, Book):
          return (self.title == other.title) and (self.isbn == other.isbn)
        else:
          return False
    def __ne__(self, other):
      return (not self.__eq__(other))

    
    def add_rating(self, rating):
        if rating is not None:
            if 0 < rating <= 4:
                self.ratings.append(rating)
                #print(self.title, self.ratings)
            else:
                print("Invalid Rating")
    

    def get_average_rating(self):
        rating_count = 0
        books_read = 0
        for rating in self.ratings:
            if rating is not None:
                rating_count += rating
                books_read += 1
                #print(self.title, rating_count, books_read)
        if books_read == 0:
            print("This book hasn't got any ratings.")
        else:        
            average_rating = rating_count / books_read
            return average_rating          
                
        
    #as the dictionary uses lists as keys need to make Book hashable
    def __hash__(self):
        return hash((self.title, self.isbn))

    
# Create a fiction subclass
class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
        
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)
    
# Create a non-fiction subclass
class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            if self.level[0] == vowel:
                return "{}, an {} manual on {}".format(self.title, self.level, self.subject)
            else:
                return "{}, a {} manual on {}".format(self.title, self.level, self.subject)
            
            
#create TomeRater
class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=None):
        if not self.users.get(email): 
            print("No user with email {email}!".format(email=email))
        else:
            user = self.users[email]
            user.read_book(book, rating)
            book.add_rating(rating)
            if not self.books.get(book):
                self.books[book] = 1
            else:
                self.books[book] += 1
                
    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if not user_books == None:
            for book in user_books:
                self.add_book_to_user(book, email, rating=None)
                
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
            
    def print_users(self):
        for user in self.users.keys():
            print(user)
            
    def print_ratings(self):
        for rating in self.books.values():
            print(rating)        
            
    
    def most_read_book(self):
        book_name = ""
        book_count = 0
        for book in self.books.keys():
            if self.books[book] > book_count:
                book_name = book.title
                book_count = self.books[book]
                #print(book_name, book_count)
        print(book_name, book_count)
        
    
    def highest_rated_book(self):
        book_name = ""
        book_rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > book_rating:
                book_name = book.title
                book_rating = book.get_average_rating()
        print(book_name, book_rating)      
        
    
    def most_positive_user(self):
        user_name = ""
        user_rating = 0
        for user in self.users.values():
            if user.get_average_rating() is not None:
                average = user.get_average_rating()
                if average > user_rating:
                    user_name = user.name
                    user_rating = average
        print(user_name, user_rating)
        
   
    
    def get_list_of_most_read_book(self):
        list_of_book_read = []
        book_name = ""
        book_count = 0
        for book in self.books:
            book_name = book.title
            book_count = self.books[book]
            list_of_book_read.append([book_name, book_count])
        return list_of_book_read
        print(list_of_book_read)
                
        
            
          