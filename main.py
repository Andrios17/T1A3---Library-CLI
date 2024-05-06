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

def display_library():
     pass

def main():
    check_json()
    while True:
        print('')
        print('************LIBRARY DIRECTORY************')
        print('Please choose from the following options')
        print('1) Add a book to the library')
        print('2) Find a book in the library')
        print('3) Display all books in the library')
        print('4) Place a book on loan')
        print('5) View all loaned books')
        print('6) Return a book to the library')
        print('7) Quit')
        print('*****************************************')
        print('')

        user_input = int(input('Enter your choice:  '))

        if user_input == 7:
            os.system('clear')
            print('Goodbye!')
            break
        elif user_input == 1:
            add_book()

if __name__ == '__main__':
    main()