# Library Management Program

## Link to GitHub Repository

[Library Management Tool GitHub Repository](https://github.com/Andrios17/T1A3---Library-CLI)

## Overview

This program was completed as a requirement of the Higher Education Diploma as a part of the Coder Academy Bootcamp.

This program is intended to be utilised by liberians. It is a library management tool which allowes users to completly self manage all inventory within their library.

It provides the user with a multitude of features which allow them to add books to their library, place books on loan and store loanee information, view books which have exceeded the loan period and return these books back to the library among many others.

Please note due to time contraints, it is advised that individuals who are using this program refrain from adding duplicate books to their library. This is a feature that can be implemented in future updates. 

## How to install this program

### Prerequisites for this program

1. Please ensure you have Python 3.12.3 installed. This can be downloaded by following the prompts in the following link: [Python Installation](https://www.python.org/downloads/)

2. Please ensure you have PIP installed. This can be downloaded by following the prompts in the following link: [PIP Installation](https://pypi.org/project/pip/)

3. Please ensure you have GitHub installed and a SSH key setup. This can be downloaded by following the prompts in the following link: [GitHub Installation](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)

### Installation guide

1. Enter your terminal and ensure you are in the correct location you wish to download the program. Once you are there, make a new directory with your 
desured name ```mkdir 'desired_name'```. 

2. Run the following command ```cd 'desired_name```. 

3. Clone the GitHub repository which contains this program into the directory you just created. This can be completed by entering the command ```git clone git@github.com:Andrios17/T1A3---Library-CLI.git```

4. Perform the command ```cd 'repo_name'``` to enter the repository.

5. Perform the command ```cd src``` to enter the source file.

6. Perform the command ```./run.sh ``` to begin the program. Please note if you recieve an error code at this point, please run the command ```chmod +x run.sh```. This will change the file permissions of the shell script to ensure it is able to be run by anyone.  

## Dependencies of the program.

There are two dependencies in this program. These include;

* art==6.2

* color_terminal==1.0

These dependecies are automatically downloaded when following the installation guide. 

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

This feature allowes users to set the loan period of their library. I wanted the user to be able to change this period as it is realistic for a library to change the policy regarding the length in which they allow their books to be loaned out to individuals.

The loan period which is entered by the user is saved and writen into the loan_period.txt file which was created when the user runs the program for the first time. This ensures that all aspects of the program is stable and useable for reusabilty of the program. For example, a user can exit and program all together and have the peace of mind that everything will be saved. 

The function begins by prompting the user to enter the loan period which they would like to set for their library.

This value is then converted into an int to allow for comparisons in the proceeding ``if`` and ``else`` statements. 

Once the user has inputed their period, the txt file which stores this data and opened and overwritten with the new data. The user will be notified of its success, however this will only occur if the ``int`` provided is greater than 0. 

If it is not, the user will be prompted to enter an ``int`` which is valid.

### Terminal Output

![Set loan period](/docs/Loan_P_O.png)

### Placing a book on loan - Feature

### Code Snippet

![Loan Book](/docs/Loan_C.png)

The code snippet above shows the backbone of the logic to allow users to place a book on loan. 

It firstly calls the upon the ```display_lubrary_multi_function()``` which displays all books in the library to the user. This allowes the user to view all books in the library for ease access. 

The user will prompted to enter a book as long as there is a book in the library. Once the user has entered the book they desire to place on loan, they will be prompted to add the loanees Name, Contact PH and Address details. All of which will be added to the dictionary of the book which is located in the JSON file.

When this occurs, the loan will be time stamped using the ```time_stamp()``` function. This is completed to allow the user to view any overdue books in another feature of the program.

This code is able to determine whether the book which the user is trying to enter is already loaned or not found in the library. The corresponding outcome will be displayed to the user. 

At the end of the logic, the user is prompted to either enter another book to be loaned or return to the main menu.

### Terminal Output

![Loan Book](/docs/Loan_O.png)

### View all loaned books or overdue books - Feature

### Code Snippet

![View All loaned books](/docs/View_L_C.png)

The code snippet above depicts the logic to allow users to either view all loaned books or view books which are overdue. 

The beginning of the logic allowes the user to enter which of the choices they desire to complete. Their input is passed into a ```match``` which will complete the desired case. 

```Case 1``` will output all loaned books to the user. This will be completed through iterating through the JSON file and printing all books which hold the value of ```True``` in key ```Loaned```. If there are no books which hold this paramater, the user will be notified and they will be returned to the main menu. 

```Case 2``` will output all overdue books to the user. This will complete the same logic of ```Case 1```, however extra logic is added to determine the current time, which is compared to the timestamp which is included on the book when it is loaned in the previous feature. The difference in these days is calculated in ```difference```. The difference is then compared to the loan period set by user by opening the txt.file and passing this value into the following ```if``` statement: ```if difference >= timedelta(days=time_allowed):```. If difference is greater to or equal to the loan period, the book's dictionary, along with the amount of days it is overdue is displayed to the user. Again, if there are no overdue books, the user will be notified and prompted to return to the main menu.

### Terminal Output

### Case 1 - View all loaned books

![View All loaned books](/docs/View_L_O_1.png)

### Case 2 - View all overdue books

![View All Overude Books](/docs/View_L_O_2.png)

### Return a book to the library - Feature

### Code Snippet

![Return a book to the library](/docs/Return_C.png)

The above code demonstrates the logic created to allow a user to return a book to the library which has been loaned. 

It firstly call upon the ```display_loaned_library_mult()``` function which will display all loaned books in the library. This function will return a result of ```True``` if there are no books in the library and if this is the case, the user will be notified of this result and the program will return to the main menu. 

However, if there are loaned books, the user will be prompted to enter the title of the book they desire to return to the library. The JSON file holding the data of the library books will be opened and iterated over to find the book which is being returned. Once found, the ```Loaned``` key will return to ```False``` and the keys which pertain to the loan status will be popped and removed. 

If the book which is inputted is not on loan, the user will be notified. This will also occur if the book which is inputted does not exist in the library all together. 

The ```repeat(use_case)``` is then called upon to provide the user with the choice to either enter another book to be returned, or retrun to the main menu. 

### Terminal Output

![Return a book to the library](/docs/Return_O.png)

### Remove a book from the library - Feature

### Code Snippet

![Remove a book from the library](/docs/Remove_C.png)

The logic for removing a book is demonstrated above. 

The code first calls the upon the ```display_library_multi_function()``` which will display all books in the library and return a value depending on whether there are any books in the library. ```False``` if there books, and ```True``` if there isnt. This is the same logic explained above in the previous feature. 

Once the user inputs the title of the book they are looking to remove, the JSON file then be opened and iterated through to find the desired book. Once it is found, the book will be removed from the JSON file. 

Once this is completed, the updated JSON file will be written into JSON file using the ```json.dump()``` method. 

### Terminal Outout

![Remove a book](/docs/Remove_O.png)

## Project Management & Implementation Plan

Trello was utilised as the project management software to create the implementation plan for this project.

A link to the trello bored for this program can be found here [Trello Board](https://trello.com/invite/b/zP8fBwk3/ATTI2b5bddbcb8861c2e01cd449b0e843ccdBE626378/library-management-program)

I also Trello exensively during the development process of this program. However, with this being said, the dates which were created as deadlines had to be altered extensively due to the fact I recieved a week long extension for this assessment task. I opted to keep the original dates in the trello bored to examplify the original plan for the assignment. However, each feature was completed in the following week on the corresponding days of the dates provided. 

I instead utilised the trello bored as more of a guidline to the spacing between tasks and it was extremely helpful to have all the features and tasks which need to be completed laid out cleanly. All features and tasks contain an extensive checklist which need to be ticked off prior to completion. 

I created the Trello prior to beginning my code for this project on the 5th of May 2024 . However, I neglected to screenshot the outcome. The below screenshot is a snippet of the full Trello bored prior to completion and was taken on the 14th of May 2024, when I returned to complete my assignment.

### Screenshot on the 14th of May 2024

![Trello Screen Shot 14/05/2024](/docs/Trello_W1.png)

As you can see, the due dates read as overdue due to the fact I had to take a week long break from completing the assignment due to illness. However, everything is extensively laid out and plan for the assignment is in place. 

### Screenshot of feature plan checklist

![Trello Checklist](/docs/Trello_Checklist.png)

This image is an example of a checklist which has been created for the Set Loan Feature. It is extensive and provides clear steps which need to be completed prior to each feature being marked as completed. This was extremely helpful process and kept the development process clear for me.

### Screenshot on the 19th of May 2024

![Trello Screen Shot 19/05/2024](/docs/Trello_Complete.png)

This image captures my completed Trello bored. As you can see, all features have been implemented and completed successfully.