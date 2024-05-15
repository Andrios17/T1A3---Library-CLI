import json, os

book_collection = []

def check_json():
    if os.path.exists('book_collection'):
        with open('book_collection', 'r') as f:
            book_collection = json.load(f)
    else:
        with open('book_collection', 'w') as f:
            book_collection = []
            json.dump(book_collection, f, indent=4)

def add_book():
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

def find_book():
    title = input('Name of the book: ')
    book_found = None
    os.system('clear')
    with open('book_collection', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            if book['Title'] == title:
                print(book)
                book_found = book
                input('Press Enter to return to the directory: ')
                return
        if book_found is None:
            print('Book not found')
    input('Press ENTER to return to the directory: ')

def display_library():
    with open('book_collection', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            print(book)
    input('Press Enter to return to the directory: ')

def loan_book():
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
    input('Press Enter to return to the directory: ')

def remove_book():
    title = input('Name of the book: ')
    removed_book = None
    with open('book_collection', 'r') as f:
        book_collection = json.load(f)
        for book in book_collection:
            if book['Title'] == title:
                book_collection.remove(book)
                removed_book = book
        with open('book_collection', 'w') as f:
            json.dump(book_collection, f, indent=4)
    input('Press Enter to return to the directory: ')

def main():
    check_json()
    while True:
        os.system('clear')
        print('')
        print('************LIBRARY DIRECTORY************')
        print('Please choose from the following options')
        print('1) Add a book to the library')
        print('2) Find a book in the library')
        print('3) Display all books in the library')
        print('4) Place a book on loan')
        print('5) View all loaned books')
        print('6) Return a book to the library')
        print('7) Remove a book from the library')
        print('8) Quit')
        print('*****************************************')
        print('')

        user_input = int(input('Enter your choice:  '))

        if user_input == 8:
            os.system('clear')
            print('Goodbye!')
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