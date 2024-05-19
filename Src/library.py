import json
import os
from datetime import datetime, timedelta

import colorterminal
from art import text2art

book_collection = []
txt_data = '0'

# Function to clear the OS terminal, will work for all OS'
def clear_OS():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Will return the date that a book is loaned
def time_stamp():
    return datetime.now().strftime('%d-%m-%Y')

# Will check if a json file exists to store all books, will create one if necessary
def check_json():
    if os.path.exists('book_collection.json'):
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
    else:
        with open('book_collection.json', 'w') as f:
            book_collection = []
            json.dump(book_collection, f, indent=4)

# Will check if a txt file exists to store the loan period, will create one if necessary
def check_txt():
    if os.path.exists('loan_period.txt'):
        with open('loan_period.txt', 'r') as f:
            txt_data = f.readlines()
    else:
        with open('loan_period.txt', 'w') as f:
            txt_data = '0'
            f.writelines(txt_data)

# Allows the content of the txt file to be displayed
def display_txt():
    with open('loan_period.txt', 'r') as f:
        txt_data = f.read()
        cleaned_data = txt_data.strip("[]")
        return cleaned_data

# A function that will repeat the below code. Used multiple times to guide the user around the program
def repeat(use_case):
    print('')
    user_choice = 0
    while user_choice != '1' or user_choice != '2':
        user_choice = input(f'{colorterminal.ColorText.YELLOW}Press 1 to {use_case} another book or 2 to return to the directory: ' + colorterminal.ColorText.WHITE)
        if user_choice == '1':
            break
        elif user_choice == '2':
            return False
        else:
            print(colorterminal.ColorText.RED +  'INVALID INPUT')
            continue 

# Used to print the multiple headings through out the program
def print_heading(heading_text):
    print(colorterminal.ColorText.PURPLE + text2art(heading_text) + colorterminal.ColorText.WHITE)

# Function which operates the Add Book feature
def add_book():
    while True:
        clear_OS()
        print_heading('---ADD A BOOK TO THE LIBRARY---')
        title = input(colorterminal.ColorText.YELLOW + 'Name of the book: ' + colorterminal.ColorText.WHITE)
        author = input(colorterminal.ColorText.YELLOW + 'Author of the book: ' + colorterminal.ColorText.WHITE)
        year_published = input(colorterminal.ColorText.YELLOW + 'Year the book was published: ' + colorterminal.ColorText.WHITE)
        loaned = False
        book_details = {'Title': title, 'Author': author, 'Year': year_published, 'Loaned': loaned}
        book_collection.append(book_details)
        with open('book_collection.json', 'r') as f:
            f_data = json.load(f)
            f_data.append(book_details)
        with open('book_collection.json', 'w') as f:
            json.dump(f_data, f, indent=4)
            print(colorterminal.ColorText.GREEN+ 'BOOK ADDED TO LIBRARY SUCCESSFULLY')
        result = repeat('add')
        if result is False:
            return

# Function which operates the Find Book feature, will iterate through the json file and return the correct book
def find_book():
    while True:
        clear_OS()
        print_heading('---FIND A BOOK---')
        title = input(colorterminal.ColorText.YELLOW + 'Name of the book: ' + colorterminal.ColorText.WHITE)
        book_found = None
        clear_OS()
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    clear_OS()
                    print_heading('---FIND A BOOK---')
                    print(colorterminal.ColorText.GREEN + 'BOOK FOUND\n' + colorterminal.ColorText.WHITE)
                    print(book)
                    book_found = book
            if book_found is None:
                clear_OS()
                print_heading('---FIND A BOOK---')
                print(colorterminal.ColorText.RED + 'Book not found')
        result = repeat('find')
        if result is False:
            return


# Function which operates the Display Library feature, will iterate over the json file and return all book data
def display_library():
    books_in_library = None
    print_heading('---LIBRARY---')
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
            books_in_library = book
    if books_in_library is None:
        print(colorterminal.ColorText.RED+ 'There are currently no books in the library')
        print(colorterminal.ColorText.RED + 'Please use the add books feature')
    input(colorterminal.ColorText.GREEN + 'Press Enter to return to the directory: ')

# Function which operates the Display Library feature, will iterate over the json file and return all book data
# Utilised in features which need the library to be displayed for usability
def display_library_multi_function():
    books_in_library = None
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
            books_in_library = book
    if books_in_library is None:
        return True 

# Will iterate over the json file and return all loaned book data
# Utilised in features which need the loan books to be displayed for usability
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

# Operates the loan book feature, will iterate over the json file and change the 'Loaned' key to True
# Also adds extra keys corresponding to the loanees details
def loan_book():
    while True:
        clear_OS()
        print_heading("--------LOAN A BOOK--------")
        result = display_library_multi_function()
        print('')
        if result is True:
            print(colorterminal.ColorText.RED + 'There are currently no books in the library')
            input(colorterminal.ColorText.YELLOW + 'Please press any key to continue')
            break
        title = input(colorterminal.ColorText.YELLOW + 'Name of the book: ' + colorterminal.ColorText.WHITE)
        loaned_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is False:
                    book['Loaned'] = True
                    loaned_book = book
                    time_loaned= time_stamp()
                    book['Loaned Date'] = time_loaned
                    book['Loanee'] = input(colorterminal.ColorText.YELLOW +'Please enter loanees name: ' + colorterminal.ColorText.WHITE)
                    book['Contact PH'] = input(colorterminal.ColorText.YELLOW +'Please enter loanee phone number: ' + colorterminal.ColorText.WHITE)
                    book['Contact Address'] = input(colorterminal.ColorText.YELLOW + 'Please enter loanee address: ' + colorterminal.ColorText.WHITE)
                    print(f'{colorterminal.ColorText.GREEN}\nBOOK LOANED SUCCESSFULLY')
                elif book['Title'] == title and book['Loaned'] is True:
                    print(colorterminal.ColorText.RED + 'This book is already on loan')
                    loaned_book = book
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if loaned_book is None:
            print(colorterminal.ColorText.RED + 'Book not found')
        result = repeat('loan')
        if result is False:
            break

# Operates the display loaned books feature, will iterate through the json file and return all books on loan for match 1
# Match 2 will return all books which are considered overdue
def display_loaned_books():
    print_heading("LOANED BOOKS")
    choice = input(colorterminal.ColorText.YELLOW + 'Please enter 1 to view all loaned books or 2 to view overdue books: ' + colorterminal.ColorText.WHITE)
    match choice:
        case '1':
            clear_OS()
            print_heading("LOANED BOOKS")
            books_on_loan = None
            with open('book_collection.json', 'r') as f:
                book_collection = json.load(f)
                for book in book_collection:
                    if book['Loaned'] is True:
                        print(book)     
                        books_on_loan = book
                if books_on_loan is None:
                    print(colorterminal.ColorText.RED + 'There are currently no books on loan')
            input(colorterminal.ColorText.RED +'\nPress ANY KEY to return to the directory: ')
        case '2':
            clear_OS()
            print_heading("OVERDUE BOOKS")
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
                            print(f'{colorterminal.ColorText.YELLOW}\nThis book is currently overdue by {colorterminal.ColorText.RED}{overdue_days} days {colorterminal.ColorText.WHITE}\n')
                            books_on_loan = book
                if books_on_loan is None:
                    print(colorterminal.ColorText.RED + 'There are currently no overdue books currently on loan')
            input(colorterminal.ColorText.RED + 'Press ANY KEY to return to the directory: ')

# Operates the return book feature. Will edit the JSON file to allow loaned books to be returned to the library
def return_book():
    while True:
        clear_OS()
        print_heading('RETURN TO LIBRARY')
        outcome = display_loaned_library_mult()
        print('')
        if outcome == True:
            print(colorterminal.ColorText.RED + 'There are currently no books on loan')
            input(colorterminal.ColorText.RED + 'Press ANY KEY to return to the directory: ')
            break
        title = input(colorterminal.ColorText.YELLOW+ 'Name of the book: ' + colorterminal.ColorText.WHITE)
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
                    print(colorterminal.ColorText.GREEN + 'Book has been successfully returned to the library')
                elif book['Title'] == title and book['Loaned'] is False:
                    print(colorterminal.ColorText.RED + 'This book is not on loan')
                    return
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if returned_book is None:
            print(colorterminal.ColorText.RED + 'Book not found')
            input(colorterminal.ColorText.RED + 'Please press ANY KEY to continue')
        result = repeat('return')
        if result is False:
            break

# Operates the remove book feature, allows books to be removed from the library by altering the JSON file
def remove_book():
    while True:
        clear_OS()
        print_heading("-------REMOVE BOOKS-------")
        result = display_library_multi_function()
        print('')
        if result == True:
            print(colorterminal.ColorText.RED +'There are currently no books in the library')
            input(colorterminal.ColorText.RED +'Press ANY KEY to return to the directory: ')
            break
        title = input(colorterminal.ColorText.YELLOW + 'Name of the book: ' + colorterminal.ColorText.WHITE)
        removed_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    book_collection.remove(book)
                    removed_book = book
                    print(colorterminal.ColorText.GREEN + 'Book removed successfully')
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if removed_book is None:
            print(colorterminal.ColorText.RED + 'Book not found')
        result = repeat('remove')
        if result is False:
            break

# Allows users to set the loan period for the library
def loan_period():
    while True:
        clear_OS()
        print_heading('LOAN PERIOD')
        loan_period = input(colorterminal.ColorText.YELLOW + 'Please enter the loan period for this library in days: ' + colorterminal.ColorText.WHITE)
        loan_period_int = int(loan_period)
        if loan_period_int > 0:
            with open('loan_period.txt', 'w') as f:
                f.write(loan_period)
                print(colorterminal.ColorText.GREEN + 'Loan period successfully updated as ' + loan_period + ' days')
                input(colorterminal.ColorText.YELLOW + 'Please press ANY KEY to continue')
                break
        else:
            print(colorterminal.ColorText.RED + 'Please enter a valid loan period e.g 14')
            input(colorterminal.ColorText.YELLOW + 'Please press ANY KEY to continue')
            continue