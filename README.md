# Library Management Program

## Link to GitHub Repository

[Library Management Tool GitHub Repository](https://github.com/Andrios17/T1A3---Library-CLI)

## Overview

This program was completed as a requirement of the Higher Education Diploma as a part of the of the Coder Academy Bootcamp.

This program is intended to be utilised by liberians. It is a library management tool which allowes users to completly self manage all inventory within their library.

It provides the user with a multitude of features which allow them to add books to their library, place books on loan and store loanee information, view books which have exceeded the loan period and return these books back to the library among many others.

## Code Styling

This project was created in Python. The style guide that was adhered to during the creation of this project was PEP 8.

I have done my best to adhere to the guidelines set by PEP 8. However, as a first time developer, I had some difficulties deciphering whether my code met the requirements.

**A LINK TO THIS STYLE GUIDE CAN BE FOUND HERE:** [PEP 8](https://peps.python.org/pep-0008/)

## Features of the program

**This program provides the user with a total of nine features which include:**

* Adding a book to the library
* Finding a book within the library
* Displaying all books in the library
* Setting the standard loan period of the library
* Placing a book on loan
* Viewing all loaned books
* Viewing overdue books
* Returning loaned books to the library
* Removing books from the library

**The underlying logic, including a walkthrough of the code and user experience will be explained below:**

### Main Menu

### Code Snippet 1

![Menu Part 1](/docs/Main()1.png)

This portion of code bears the brunt of what is displayed to the user when first running the program. It outlays the different paths which can be undertaken based on the input provided by the user.

When the user first runs the program, two main functions are initiatied in the background. These include the following:

* ```library.check_json()``` - This function checks the directory to see if a .JSON file named 'book_collection' exists within the directory. If it does not, this function will create this file. File is extremely important as this file bears the brunt of the entire program and without it's existence, the entire program will fail to work. This is due to the fact that all books inputed by the user will be stored in this file.

* ``library.check_txt()``` - This function checks directory to see if a .txt file name 'loan_period' exists within the directory. If it does not, this function will create this file. This file stores the loan period inputed by the user.

### Code Snippet 2

![Menu Part 2](/docs/Main()2.png)

The user is prompted to enter an option based on the menu provided. Depending on the users choice, the program will execute a function designed to execute one of the particular features of the program.

Error handling is implemented to catch any ValueErrors which may be encountered.

The entire Main() function is wrapped in a ```while True``` loop so it is consistantly displayed to the user. However, this loop is broken if the user inputs 9 as a ```break``` utilised. This ensures continuity is presented to the user and they are exited from the program if and only they decide to do so.

### Terminal Output

![Menu Output](/docs/Main().png)

### Adding a book to the library - Feature

### Code Snippet

![Adding Code](/docs/Adding%20C.png)

The ```add_book()``` function controls the logic for adding a book to the library. The user is prompted to add the Title, Author and Year Published of the book they desire to add to their library.

These details will then create a new dictionay named ```book_details``` with each prompt being the key and the input of the user being the value. The dictionary will then be appended to an empty list.

The JSON file will then be opened and loaded into the program with the code following this allowing the new book to be added to the library database.

When the book is successfully added, the user will be notified in the terminal with a success message and will be provided with the opportunity to either add another book or return to the main menu.

### Terminal Output

![Adding Output](/docs/Adding%200.png)

### Finding a book in the library - Feature

### Code Snippet

![Finding a book in the library](/docs/Find%20C.png)

This feature allowes users to find whether a book exists within their library.
It is extremely simple in logic, however can be very useful.

The program will prompt the user to enter the title of the book they are trying to locate and assign this input to the variable ```title```. The program will then open the json file and parse the ```title``` varible through each dictionary comparing the variable to the ```['Title']``` key.

If there is a match, the program will print the entire contents of the dictionary, including the loan status of the book. The user will also be notified that their search was successful through the use of a print statement.

However, if no book is found, the program will also notify the user through the use of a print statement stating ```book not found```. 
The user is then prompted to enter either search for another book, or return to the main menu.

### Terminal Output

![Finding a book in the library](/docs/Find%20O.png)

### Display Library - Feature

### Code Snippet

![Display all books](/docs/Display%20C.png)

Again, the code utilsied to perform this feature is simple in its implementation.

When the user enters the prompt to perform this feature, the program will open the JSON file used to store all the dictionarys created to store the books. It will then display each book to the terminal.

If the there are no books stored in the JSON file. The user will be notified and guided to revert to the add books feature to begin building their library so any books added can be displayed.

There is a prompt to return the main menu which the user can initiate when they are finished viewing the library.

### Terminal Output

![Display all books](/docs/Display%20O.png)

### Set Loan Period - Feature

### Code Snippet

![Set loan period](/docs/Loan_P_C.png)

This feature allowes users to set the loan period of their library. I wanted the user to be able to change this period as it is realistic for a library to change the policy regarding the length in which they allow their books to be loaned out to patrons.

The loan period which is entered by the user is saved and writen into the loan_period.txt file which was created when the user runs the program for the first time. This ensures that all aspects of the program is stable and useable for reusabilty of the program. For example, a user can exit and program all together and have the peace of mind that everything will be saved. 

The function begins by prompting the user to enter the loan period which they would like to set for their library.

This value is then converted into an int to allow for comparisons in the proceeding ``if`` and ``else`` statements. 

Once the user has inputed their period, the txt file which stores this data and opened and overwritten with the new data. The user will be notified of its success, however this will only occur if the ``int`` provided is greater than 0. 

If it is not, the user will be prompted to enter an ``int`` which is valid.

### Terminal Output

![Set loan period](/docs/Loan_P_O.png)

### Placing a book on loan - Feature

