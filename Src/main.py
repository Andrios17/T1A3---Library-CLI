import json
import os
import Src.library as library
from datetime import datetime, timedelta

from color50 import rgb, constants
from art import *

my_color = rgb(0, 0, 255)
options_color = rgb(255, 128, 0)
error_color = rgb(255, 0, 0)

def main():
    library.clear_OS
    library.check_json()
    library.check_txt()
    directory = text2art("LIBRARY DIRECTORY")
    end_bracket = text2art("----------------")
    goodbye = text2art("GOODBYE!")
    while True:
        library.clear_OS()
        print('')
        print(my_color + directory + constants.RESET)
        print(options_color + 'PLEASE CHOOSE FROM THE FOLLOWING OPTIONS' + constants.RESET)
        print('')
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
                library.clear_OS()
                print(options_color + goodbye + constants.RESET)
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
                print(options_color + 'Setting a Loan Period is Required When First Using This Program!' + constants.RESET)
                option = str(input(options_color + 'Please Enter 1 To Set The Standard Loan Period, OR Enter ANY OTHER KEY If It Is Already Set: ' + constants.RESET))
                if option == '1':
                    library.loan_period()
                library.loan_book()
            elif user_input == 5:
                library.clear_OS()
                library.display_loaned_books()
            elif user_input == 6:
                library.clear_OS()
                library.return_book()
            elif user_input == 7:
                library.clear_OS()
                library.remove_book()
            else:
                print(options_color + 'Invalid Input' + constants.RESET)
                continue
        except Exception:
            print(error_color + 'INVALID INPUT' + constants.RESET)
            input(options_color + 'Please press any key to continue: ' + constants.RESET)

if __name__ == '__main__':
    main()