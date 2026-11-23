import re

try:
    book_title = input("Enter book title: ")
    publication_year = input("Enter publication year: ")

    if re.search("^[A-Za-z ]+$", book_title):
        print("Book title:", book_title)
    else:
        raise ValueError("Invalid book title")

    if re.search("^(19|20)[0-9]{2}$", publication_year):
        print("Publication year:", publication_year)
    else:
        raise ValueError("Invalid publication year")

except ValueError as error:
    print("Error:", error)

finally:
    print("Library system execution completed")