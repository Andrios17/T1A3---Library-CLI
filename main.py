import json, os
from color50 import rgb, constants
from art import *

book_collection = []

class Quit(Exception):
    pass

def check_json():
    if os.path.exists('book_collection'):
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
    else:
        with open('book_collection', 'w') as f:
            book_collection = []
            json.dump(book_collection, f, indent=4)

def add_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
        author = input('Author of the book: ')
        year_published = input('Year the book was published: ')
        loaned = False
        book_details = {'Title': title, 'Author': author, 'Year': year_published, 'Loaned': loaned}
        book_collection.append(book_details)
        with open('book_collection', 'r') as f:
            f_data = json.load(f)
            f_data.append(book_details)
        with open('book_collection', 'w') as f:
            json.dump(f_data, f, indent=4)
            print('Book added')
        result = repeat('add')
        if result is False:
            return

def find_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
        book_found = None
        os.system('clear')
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    print(book)
                    book_found = book
            if book_found is None:
                print('Book not found')
        result = repeat('find')
        if result is False:
            return

def display_library():
    books_in_library = None
    with open('book_collection', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
            books_in_library = book
    if books_in_library is None:
        print('There are currently no books in the library')
    input('Press Enter to return to the directory: ')

def loan_book():
    while True:
        title = input('Name of the book: ')
        loaned_book = None
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is False:
                    book['Loaned'] = True
                    loan_book = book
                elif book['Title'] == title and book['Loaned'] is True:
                    print('This book is already on loan')
                    return
            with open('book_collection', 'w') as f:
                json.dump(book_collection, f, indent=4)
        input('Press Enter to return to the directory: ')
        result = repeat('loan')
        if result is False:
            break

def display_loaned_books():
    books_on_loan = None
    with open('book_collection', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            if book['Loaned'] is True:
                print(book)     
                books_on_loan = book
        if books_on_loan is None:
            print('There are currently no books on loan')
    input('Press Enter to return to the directory: ')

def return_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
        returned_book = None
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is True:
                    book['Loaned'] = False
                    returned_book = book
                elif book['Title'] == title and book['Loaned'] is False:
                    print('This book is not on loan')
                    return
            with open('book_collection', 'w') as f:
                json.dump(book_collection, f, indent=4)
        result = repeat('return')
        if result is False:
            break

def remove_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
        removed_book = None
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    book_collection.remove(book)
                    removed_book = book
                elif book['Title'] != title:
                    print('Book not found')
            with open('book_collection', 'w') as f:
                json.dump(book_collection, f, indent=4)
        result = repeat('remove')
        if result is False:
            break

def repeat(use_case):
    user_choice = 0
    while user_choice != '1' or user_choice != '2':
        user_choice = input(f'Press 1 to {use_case} another book or 2 to return to the directory: ')
        if user_choice == '1':
            break
        elif user_choice == '2':
            return False
        else:
            print('Invalid input')
            continue 

def main():
    check_json()
    my_color = rgb(0, 0, 255)
    options_color = rgb(255, 128, 0)
    directory = text2art("LIBRARY DIRECTORY")
    end_bracket = text2art("----------------")
    goodbye = text2art("GOODBYE!")
    
    while True:
        os.system('clear')
        print('')
        print(my_color + directory + constants.RESET)
        print(options_color + 'Please choose from the following options' + constants.RESET)
        print('1) Add a book to the library')
        print('2) Find a book in the library')
        print('3) Display all books in the library')
        print('4) Place a book on loan')
        print('5) View all loaned books')
        print('6) Return a book to the library')
        print('7) Remove a book from the library')
        print('8) Quit')
        print(my_color + end_bracket + constants.RESET)
        print('')


        user_input = int(input(options_color + 'Enter your choice:  ' + constants.RESET))

        if user_input == 8:
            os.system('clear')
            print(options_color + goodbye + constants.RESET)
            break
        elif user_input == 1:
            os.system('clear')
            add_book()
        elif user_input == 2:
            os.system('clear')
            find_book()
        elif user_input == 3:
            os.system('clear')
            display_library()
        elif user_input == 4:
            os.system('clear')
            loan_book()
        elif user_input == 5:
            os.system('clear')
            display_loaned_books()
        elif user_input == 6:
            os.system('clear')
            return_book()
        elif user_input == 7:
            os.system('clear')
            remove_book()
    
if __name__ == '__main__':
    main()