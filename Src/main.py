import json
import os
from datetime import datetime, timedelta

from art import *
import colorterminal
import library



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
        print(colorterminal.ColorText.PURPLE + directory)
        print(colorterminal.ColorText.YELLOW+ 'PLEASE CHOOSE FROM THE FOLLOWING OPTIONS')
        print('')
        print(colorterminal.ColorText.PURPLE + '1)' + colorterminal.ColorText.WHITE + ' Add a book to the library')
        print(colorterminal.ColorText.PURPLE + '2)' + colorterminal.ColorText.WHITE + ' Find a book in the library')
        print(colorterminal.ColorText.PURPLE + '3)' + colorterminal.ColorText.WHITE + ' Display all books in the library')
        print(colorterminal.ColorText.PURPLE + '4)' + colorterminal.ColorText.WHITE + ' Place a book on loan')
        print(colorterminal.ColorText.PURPLE + '5)' + colorterminal.ColorText.WHITE + ' View all loaned books')
        print(colorterminal.ColorText.PURPLE+ '6)' + colorterminal.ColorText.WHITE + ' Return a book to the library')
        print(colorterminal.ColorText.PURPLE + '7)' + colorterminal.ColorText.WHITE + ' Remove a book from the library')
        print(colorterminal.ColorText.PURPLE + '8)' + colorterminal.ColorText.WHITE + ' Quit')
        print(colorterminal.ColorText.PURPLE + end_bracket)
        print('')

        try:
            user_input = int(input(colorterminal.ColorText.YELLOW + 'Enter your choice: ' + colorterminal.ColorText.WHITE))
            if user_input == 8:
                library.clear_OS()
                print(colorterminal.ColorText.PURPLE + goodbye)
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
                print(colorterminal.ColorText.PURPLE + 'Setting a Loan Period is Required When First Using This Program!')
                option = str(input(colorterminal.ColorText.YELLOW + 'Please Enter 1 To Set The Standard Loan Period, OR Enter ANY OTHER KEY If It Is Already Set: '))
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
                print(colorterminal.ColorText.RED+ 'Invalid Input')
                continue
        except Exception:
            print(colorterminal.ColorText.RED + 'INVALID INPUT')
            input(colorterminal.ColorText.YELLOW + 'Please press any key to continue: ')

if __name__ == '__main__':
    main()