#The books available to buy online are as follows.
book_name1 = "Book 1: The Thursday Murder Club by Richard Osman"
book_cost1 = 8.00
book_description1 = "In a peaceful retirement village, four unlikely friends meet up once a week to investigate unsolved murders."

book_name2 = "Book 2: The Midnight Library by Matt Haig"
book_cost2 = 12.00
book_description2 = "When Nora Seed finds herself in the Midnight Library, she has a chance to make things right. Things are about to change."

book_name3 = "Book 3: The Family Upstairs by Lisa Jewell"
book_cost3 = 4.50
book_description3 = "In the kitchen lie three decomposing corpses. Close to them is a hastily scrawled note."

#The user is offered the different book options.
print("The three amazing books we have on offer this week are as follows:")
"\n"
print()
print(book_name1)
print(book_description1)
"\n"
print(book_cost1)
print()
print(book_name2)
print(book_description2)
"\n"
print(book_cost2)
print()
print(book_name3)
print(book_description3)
"\n"
print(book_cost3)
"\n"
print()

#The user now selects the book option they want.
"\n"
question = int(input('Out of these options (Book 1, Book 2, Book 3), which book would you like to purchase?'))
if question == 1:
        print(book_name1, book_cost1)
        print("The book you have selected has been added to your basket. Please click to check out.")
elif question == 2:
        print(book_name2, book_cost2)
        print("The book you have selected has been added to your basket. Please click to check out.")
elif question == 3:
        print(book_name3, book_cost3)
        print("The book you have selected has been added to your basket. Please click to check out.")
else:
        print('Sorry. That\'s not an option!')
        
