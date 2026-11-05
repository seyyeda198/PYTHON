receipt_header = """
 BOOKSTORE RECEIPT
"""

book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

product1 = "\nBook: {}\tPrice: {}".format(book1, price1)
product2 = "\nBook: {}\tPrice: {}".format(book2, price2)

total = price1 + price2
total_price = "\nTotal Price: {}".format(total)

message = "\nThank you for visiting our bookstore."

receipt = receipt_header + product1 + product2 + total_price + message

print(receipt.upper())