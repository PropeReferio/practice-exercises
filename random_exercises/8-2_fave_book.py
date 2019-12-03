# Python Crash Course 8-2. Favorite Book: Write a function called 
#favorite_book() that accepts one parameter, title . The function should 
#print a message, such as One of my favorite books is Alice in Wonderland .
# Call the function, making sure to include a book title as an argument in the function call .

def fave_book(title):
    print(f"One of my favorite books is {title}.")

fave_book(input("What is one of your favorite books?" ))