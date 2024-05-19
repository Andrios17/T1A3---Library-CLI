import json
import os
from datetime import datetime, timedelta

from art import *
import colorterminal
import library

#Main function, will be called when running bash scripts
def main():
    library.clear_OS
    library.check_json()
    library.check_txt()
    while True:
        library.clear_OS()
        library.print_heading('----------------')
        library.print_heading('LIBRARY DIRECTORY')
        print(colorterminal.ColorText.YELLOW+ 'PLEASE CHOOSE A NUMBER FROM THE FOLLOWING OPTIONS')
        print('')
        print(colorterminal.ColorText.PURPLE + '1)' + colorterminal.ColorText.WHITE + ' Add a book to the library')
        print(colorterminal.ColorText.PURPLE + '2)' + colorterminal.ColorText.WHITE + ' Find a book in the library')
        print(colorterminal.ColorText.PURPLE + '3)' + colorterminal.ColorText.WHITE + ' Display all books in the library')
        print(colorterminal.ColorText.PURPLE + '4)' + colorterminal.ColorText.WHITE + ' View or set loan period of library')
        print(colorterminal.ColorText.PURPLE + '5)' + colorterminal.ColorText.WHITE + ' Place a book on loan')
        print(colorterminal.ColorText.PURPLE + '6)' + colorterminal.ColorText.WHITE + ' View all loaned books or overdue books')
        print(colorterminal.ColorText.PURPLE + '7)' + colorterminal.ColorText.WHITE + ' Return a book to the library')
        print(colorterminal.ColorText.PURPLE + '8)' + colorterminal.ColorText.WHITE + ' Remove a book from the library')
        print(colorterminal.ColorText.PURPLE + '9)' + colorterminal.ColorText.WHITE + ' Exit Directory')
        library.print_heading('----------------')
        print('')

# if/elif statements wrapped in a try/else block. Will handle the input from users and run the corresponding method to the feature selected.
        try:
            user_input = int(input(colorterminal.ColorText.YELLOW + 'Enter your choice: ' + colorterminal.ColorText.WHITE))
            if user_input == 9:
                library.clear_OS()
                library.print_heading('GOODBYE')
                break
            elif user_input == 1:
                library.clear_OS()
                library.add_book()
            elif user_input == 2:
                library.clear_OS()
                library.find_book()
            elif user_input == 3:
                library.clear_OS()
                library.display_library()
            elif user_input == 4:
                library.clear_OS()
                library.print_heading('LOAN PERIOD')
                print(f'{colorterminal.ColorText.RED}THE CURRENT LOAN PERIOD IN DAYS IS: {colorterminal.ColorText.GREEN}{library.display_txt()}\n')
                option = str(input(colorterminal.ColorText.YELLOW + '''PLEASE ENTER 1 TO RESET THE LOAN PERIOD\nOR\nPRESS ANY OTHER KEY TO EXIT IF DATE IS SET CORRECTLY: '''))
                if option == '1':
                    library.loan_period()
            elif user_input == 5:
                library.loan_book()
            elif user_input == 6:
                library.clear_OS()
                library.display_loaned_books()
            elif user_input == 7:
                library.clear_OS()
                library.return_book()
            elif user_input == 8:
                library.clear_OS()
                library.remove_book()
            else:
                print(colorterminal.ColorText.RED+ 'Invalid Input')
                continue
        except Exception:
            print(colorterminal.ColorText.RED + 'INVALID INPUT')
            input(colorterminal.ColorText.YELLOW + 'Please press any key to continue: ')

if __name__ == '__main__':
    main()