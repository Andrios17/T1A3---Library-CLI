import json
import os
from datetime import datetime, timedelta

from color50 import rgb, constants
from art import *

book_collection = []
txt_data = 'Hello World'
my_color = rgb(0, 0, 255)
options_color = rgb(255, 128, 0)
error_color = rgb(255, 0, 0)
success_color = rgb(0,128,0)

def clear_OS():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def time_stamp():
    return datetime.now().strftime('%d-%m-%Y')

def check_json():
    if os.path.exists('book_collection.json'):
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
    else:
        with open('book_collection.json', 'w') as f:
            book_collection = []
            json.dump(book_collection, f, indent=4)

def check_txt():
    if os.path.exists('loan_period.txt'):
        with open('loan_period.txt', 'r') as f:
            book_collection = f.readlines()
    else:
        with open('loan_period.txt', 'w') as f:
            f.writelines(txt_data)

def add_book():
    while True:
        clear_OS()
        heading = text2art('---ADD A BOOK TO THE LIBRARY---')
        print(my_color + heading + constants.RESET)
        title = input(options_color + 'Name of the book: ' + constants.RESET)
        author = input(options_color + 'Author of the book: ' + constants.RESET)
        year_published = input(options_color + 'Year the book was published: ' + constants.RESET)
        loaned = False
        book_details = {'Title': title, 'Author': author, 'Year': year_published, 'Loaned': loaned}
        book_collection.append(book_details)
        with open('book_collection.json', 'r') as f:
            f_data = json.load(f)
            f_data.append(book_details)
        with open('book_collection.json', 'w') as f:
            json.dump(f_data, f, indent=4)
            print(success_color + 'BOOK ADDED TO LIBRARY SUCCESSFULLY' + constants.RESET)
        result = repeat('add')
        if result is False:
            return

def find_book():
    while True:
        clear_OS()
        heading = text2art('---FIND A BOOK---')
        print(my_color + heading + constants.RESET)
        title = input(options_color + 'Name of the book: ' + constants.RESET)
        book_found = None
        clear_OS()
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    print(book)
                    book_found = book
            if book_found is None:
                print(error_color + 'Book not found' + constants.RESET)
        result = repeat('find')
        if result is False:
            return

def display_library():
    books_in_library = None
    heading = text2art('---LIBRARY---')
    print(my_color + heading + constants.RESET)
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
            books_in_library = book
    if books_in_library is None:
        print(error_color + 'There are currently no books in the library' + constants.RESET)
        print(error_color + 'Please use the add books feature' + constants.RESET)
    input(success_color + 'Press Enter to return to the directory: ' + constants.RESET)

def display_library_multi_function():
    books_in_library = None
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
            books_in_library = book
    if books_in_library is None:
        return True 


def display_loaned_library_mult():
    books_on_loan = None
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            if book['Loaned'] is True:
                print(book)     
                books_on_loan = book
    if books_on_loan is None:
        return True



def loan_book():
    while True:
        clear_OS()
        title = text2art("--------LOAN A BOOK--------")
        print(my_color + title + constants.RESET)
        result = display_library_multi_function()
        if result is True:
            print(error_color + 'There are currently no books in the library' + constants.RESET)
            input(my_color + 'Please press any key to continue' + constants.RESET)
            break
        title = input(options_color + 'Name of the book: ' + constants.RESET)
        loaned_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is False:
                    book['Loaned'] = True
                    loaned_book = book
                    time_loaned= time_stamp()
                    book['Loaned Date'] = time_loaned
                    book['Loanee'] = input(options_color + 'Please enter loanees name: ' + constants.RESET)
                    book['Contact PH'] = input(options_color + 'Please enter loanee phone number: ' + constants.RESET)
                    book['Contact Address'] = input(options_color + 'Please enter loanee address: ' + constants.RESET)
                elif book['Title'] == title and book['Loaned'] is True:
                    print(error_color + 'This book is already on loan' + constants.RESET)
                    input(my_color + 'Please press any key to continue' + constants.RESET)
                    loaned_book = book
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if loaned_book is None:
            print(error_color + 'Book not found' + constants.RESET)
        result = repeat('loan')
        if result is False:
            break

def display_loaned_books():
    choice = input(my_color + 'Please enter 1 to view all loaned books or 2 to view overdue books: ' + constants.RESET)
    match choice:
        case '1':
            books_on_loan = None
            with open('book_collection.json', 'r') as f:
                book_collection = json.load(f)
                for book in book_collection:
                    if book['Loaned'] is True:
                        print(book)     
                        books_on_loan = book
                if books_on_loan is None:
                    print(options_color + 'There are currently no books on loan' + constants.RESET)
            input(error_color +'Press Enter to return to the directory: ' + constants.RESET)
        case '2':
            books_on_loan = None
            with open('book_collection.json', 'r') as f:
                book_collection = json.load(f)
                with open('loan_period.txt') as x:
                    time_allowed = int(x.read())
                for book in book_collection:
                    if book['Loaned'] is True:
                        todays_date = datetime.now()
                        date_in_file = book['Loaned Date']
                        loaned_date = datetime.strptime(date_in_file, '%d-%m-%Y')
                        difference = todays_date - loaned_date
                        overdue_days = difference.days - time_allowed
                        if difference >= timedelta(days=time_allowed):
                            print(book)
                            print(f'This book is currently overdue by {overdue_days} days')
                            books_on_loan = book
                if books_on_loan is None:
                    print(options_color + 'There are currently no overdue books currently on loan' + constants.RESET)
            input(error_color + 'Press Enter to return to the directory: ' + constants.RESET)


def return_book():
    while True:
        clear_OS()
        heading = text2art('RETURN TO LIBRARY')
        print(options_color + heading + constants.RESET)
        outcome = display_loaned_library_mult()
        if outcome == True:
            print(error_color + 'There are currently no books on loan' + constants.RESET)
            input(error_color + 'Press Enter to return to the directory: ' + constants.RESET)
            break
        title = input(options_color + 'Name of the book: ' + constants.RESET)
        returned_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is True:
                    book['Loaned'] = False
                    returned_book = book
                    book.pop('Loaned Date')
                    book.pop('Loanee')
                    book.pop('Contact PH')
                    book.pop('Contact Address')
                    print(success_color + 'Book has been successfully returned to the library' + constants.RESET)
                elif book['Title'] == title and book['Loaned'] is False:
                    print(error_color + 'This book is not on loan' + constants.RESET)
                    return
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if returned_book is None:
            print(error_color + 'Book not found' + constants.RESET)
            input(my_color + 'Please press any key to continue' + constants.RESET)
        result = repeat('return')
        if result is False:
            break

def remove_book():
    while True:
        clear_OS()
        heading = text2art("-------REMOVE BOOKS-------")
        print(my_color + heading + constants.RESET)
        result = display_library_multi_function()
        if result == True:
            print(error_color + 'There are currently no books in the library' + constants.RESET)
            input(error_color + 'Press Enter to return to the directory: ' + constants.RESET)
            break
        title = input(options_color + 'Name of the book: ' + constants.RESET)
        removed_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    book_collection.remove(book)
                    removed_book = book
                    print(success_color + 'Book removed successfully' + constants.RESET)
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if removed_book is None:
            print(error_color + 'Book not found' + constants.RESET)
        result = repeat('remove')
        if result is False:
            break

def repeat(use_case):
    user_choice = 0
    while user_choice != '1' or user_choice != '2':
        user_choice = input(f'{error_color}Press 1 to {use_case} another book or 2 to return to the directory: ' + constants.RESET)
        if user_choice == '1':
            break
        elif user_choice == '2':
            return False
        else:
            print(error_color + 'INVALID INPUT' + constants.RESET)
            continue 

def loan_period():
    while True:
        try:
            clear_OS()
            loan_period = input(options_color + 'Please enter the loan period for this library in days: ' + constants.RESET)
            loan_period_int = int(loan_period)
            if loan_period_int > 0:
                with open('loan_period.txt', 'w') as f:
                    f.write(loan_period)
                    print(success_color + 'Loan period successfully updated as ' + loan_period + ' days' + constants.RESET)
                    input(my_color + 'Please press any key to continue' + constants.RESET)
                    break
            else:
                print(error_color + 'Please enter a valid loan period e.g 14' + constants.RESET)
                continue
        except Exception:
            print(error_color + 'Please enter a valid loan period e.g 14' + constants.RESET)
            input(my_color + 'Please press any key to continue' + constants.RESET)
            continue