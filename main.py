import json, os
from color50 import rgb, constants
from art import *
from datetime import datetime, timedelta

book_collection = []
txt_data = 'Hello World'
my_color = rgb(0, 0, 255)
options_color = rgb(255, 128, 0)
error_color = rgb(255, 0, 0)


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
        os.system('clear')
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
            print(my_color + 'BOOK ADDED TO LIBRARY SUCCESSFULLY' + constants.RESET)
        result = repeat('add')
        if result is False:
            return

def find_book():
    while True:
        os.system('clear')
        title = input(ptions_color + 'Name of the book: ' + constants.RESET)
        book_found = None
        os.system('clear')
        with open('book_collection.json', 'r') as f:
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
    with open('book_collection.json', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(f'')
            books_in_library = book
    if books_in_library is None:
        print('There are currently no books in the library')
    input('Press Enter to return to the directory: ')

def loan_book():
    while True:
        title = input('Name of the book: ')
        loaned_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title and book['Loaned'] is False:
                    book['Loaned'] = True
                    loan_book = book
                    time_loaned= time_stamp()
                    book['Loaned Date'] = time_loaned
                    book['Loanee'] = input('Please enter loanees name: ')
                    book['Contact PH'] = input('Please enter loanee phone number: ')
                    book['Contact Address'] = input('Please enter loanee address: ')
                elif book['Title'] == title and book['Loaned'] is True:
                    print('This book is already on loan')
                    input('Please press any key to continue')
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if loaned_book is None:
            print('Book not found')
        result = repeat('loan')
        if result is False:
            break

def display_loaned_books():
    choice = input('Please enter 1 to view all loaned books or 2 to view overdue books: ')
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
                    print('There are currently no books on loan')
            input('Press Enter to return to the directory: ')
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
                    print('There are currently no overdue books currently on loan')
            input('Press Enter to return to the directory: ')


def return_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
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
                elif book['Title'] == title and book['Loaned'] is False:
                    print('This book is not on loan')
                    return
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if returned_book is None:
            print('Book not found')
        result = repeat('return')
        if result is False:
            break

def remove_book():
    while True:
        os.system('clear')
        title = input('Name of the book: ')
        removed_book = None
        with open('book_collection.json', 'r') as f:
            book_collection = json.load(f)
            for book in book_collection:
                if book['Title'] == title:
                    book_collection.remove(book)
                    removed_book = book
                    print('Book removed successfully')
            with open('book_collection.json', 'w') as f:
                json.dump(book_collection, f, indent=4)
        if removed_book is None:
            print('Book not found')
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
            print('Invalid input')
            continue 

def loan_period():
    while True:
        try:
            os.system('clear')
            loan_period = input('Please enter the loan period for this library in days: ')
            loan_period_int = int(loan_period)
            if loan_period_int > 0:
                with open('loan_period.txt', 'w') as f:
                    f.write(loan_period)
                    break
            else:
                print('Please enter a valid loan period')
                continue
        except Exception:
            print('Please enter a valid loan period')
            continue

def main():
    check_json()
    check_txt()
    directory = text2art("LIBRARY DIRECTORY")
    end_bracket = text2art("----------------")
    goodbye = text2art("GOODBYE!")
    while True:
        os.system('clear')
        print('')
        print(my_color + directory + constants.RESET)
        print(options_color + 'Please choose from the following options' + constants.RESET)
        print(my_color + '1)' + constants.RESET + ' Add a book to the library')
        print(my_color + '2)' + constants.RESET + ' Find a book in the library')
        print(my_color + '3)' + constants.RESET + ' Display all books in the library')
        print(my_color + '4)' + constants.RESET + ' Place a book on loan')
        print(my_color + '5)' + constants.RESET + ' View all loaned books')
        print(my_color + '6)' + constants.RESET + ' Return a book to the library')
        print(my_color + '7)' + constants.RESET + ' Remove a book from the library')
        print(my_color + '8)' + constants.RESET + ' Quit')
        print(my_color + end_bracket + constants.RESET)
        print('')

        try:
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
                option = int(input(options_color + 'Please Enter 1 To Set The Standard Loan Period, OR Enter 2 If It Is Already Set: ' + constants.RESET))
                if option == 1:
                    loan_period()
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
            else:
                print(options_color + 'Invalid Input' + constants.RESET)
                continue
        except Exception:
            print(error_color + 'INVALID INPUT' + constants.RESET)
            input(options_color + 'Please press any key to continue: ' + constants.RESET)

if __name__ == '__main__':
    main()