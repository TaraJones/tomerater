from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
nonfiction3 = Tome_Rater.create_non_fiction("Accounting for Growth", "Economics", "intermediate", 11111000)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)
novel4 = Tome_Rater.create_novel("Great Expectations", "Charles Dickens", 10001020)
novel5 = Tome_Rater.create_novel("Cat's Cradle", "Kurt Vonnegut", 10001050)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
Tome_Rater.add_user("Christopher Columbus", "chris@columbus.org")


#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])
Tome_Rater.add_user("Mickey Mouse", "m@mouse.edu", user_books=[novel4, nonfiction3])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel4, "m@mouse.edu", 3)
Tome_Rater.add_book_to_user(novel5, "m@mouse.edu", 4)
Tome_Rater.add_book_to_user(nonfiction3, "m@mouse.edu", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel5, "marvin@mit.edu", 3)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print("Check ratings are being correctly added:")

print("\nCatalog:")
Tome_Rater.print_catalog()

print("\nUsers:")
Tome_Rater.print_users()

#print("\nRatings:")
#Tome_Rater.print_ratings()

print("\nMost read book:")
print(Tome_Rater.most_read_book())

print("\nHighest rated book:")
print(Tome_Rater.highest_rated_book())

print("\nMost positive user:")
print(Tome_Rater.most_positive_user())

print("\nMost Read book list:")
print(Tome_Rater.get_list_of_most_read_book())


