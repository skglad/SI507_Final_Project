# SI507 Final Project: Book Finder App

by Sara Gladchun

[Link to this repository](https://github.com/skglad/SI507_Final_Project)

---

## Project Description

*Preliminary work:* Before creating my program, I took the books.csv file which is a dataset of 10,000 books from Goodreads (found on kaggle.com) and used the program cleaning_books.py  to clean the dataset and drop  unnecesary columns. The data is then put into a new .csv called clean_books.csv. The clean_books.csv contains 10,000 books as well.<br>
<br>
My program takes the clean_books.csv and creates a database with two tables: **books and authors**. For the purposes of this program, I have limited the insertion of data into the database to the first 2,000 books from the dataset. When the program is run, it creates a flask app that allows a user to search through the database. Before the first request, the data is inserted into the database tables. The user can then query books by author in order to get a list of books written by the author. The user can also query books by a search term, which will return a list of books that have said search term in the title. The user can also query the database by the title of the book and the app will return an image of the book cover.

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt`
2. Download all files needed to run the program (templates folder, static folder, books_clean.csv) and make sure they are in the same directory as the program file (book_tools.py)
2. Then, you should run 'python3 book_tools.py' in your terminal
3. Once you run the program in the terminal, you can navigate to localhost5000: and use the app

## How to use

1. When the user navigates to localhost:5000 They will be taken to the homepage with links to the rest of the routes.
2. The user can navigate to the author route, which will populate a form where the user can input information and the app will return a list of books written by that author that are in the Database (for example, try "Harper Lee")
3. The user can navigate to the search route, which will populate a form where the user can input a search term (for example, try "car" or "harry" or "magic") and the app will return a list of books with titles that contain that search term.
4. The user can navigate to the book cover route that will populate a form that allows the user to input the title of a book and the app will return an image of the book's cover (for example, try "The Lovely Bones").
5. The user can always navigate to the information route which will give the user an overview of the functionality of the app.
6. It is important to note that correct spelling of the author and title are very important. The queries are not case sensitive, but correct spelling is necessary.
7. Please look in "screenshot" directory for views of what the app should look like when it is run.

## Routes in this application
- `/` -> this is the home page of the application with a welcome message and links to the other routes
- `/information` -> this route has a bit of information about what the app does and allows the user to navigate to the other routes in the app
- `/author` -> this route has a form for user input for the name of an author and will return a list of books written by the author
- `/search` -> this route has a form that will accept user input for a search term, and then returns a list of all the titles that contain the search term
- `/bookcover` -> this route also had a form that accept the title of a book and returns the image of the bookcover

## How to run tests
1. First make sure the file SI507project_tests.py is in the same directory as the rest of the files
2. Run the app program and navigate to localhost:5000 so that the database is created
3. Run the test file: SI507project_tests.py in your terminal

## In this repository:
- templates
  - author-form.html
  - author-list.html
  - background.html
  - cover-form.html
  - image.html
  - information.html
  - search-form.html
  - search-return.html
- static
  - colors.js
- screenshots
  - Results_author_form.png
  - Results_author_search.png
  - Results_homepage.png
  - Results_image.png
  - Results_search_term.png
- book_tools.py
- books_clean.csv
- cleaning_books.py - code used to clean original dataset
- books.csv - original dataset downloaded from kaggle (contains 10,000 books from Goodreads)
- books.db_project_final
- requirements.txt
- SI507 Final Project Database Diagram.pdf
- SI507project_test.py
- README.md
---

### General
- [X] Project is submitted as a Github repository
- [X] Project includes a working Flask application that runs locally on a computer
- [X] Project includes at least 1 test suite file with reasonable tests in it.
- [X] Includes a `requirements.txt` file containing all required modules to run program
- [X] Includes a clear and readable README.md that follows this template
- [X] Includes a sample .sqlite/.db file
- [X]  Includes a diagram of your database schema
- [X] Includes EVERY file needed in order to run the project
- [X] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [X] Includes at least 3 different routes
- [X] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [X] Interactions with a database that has at least 2 tables
- [X] At least 1 relationship between 2 tables in database
- [X] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [X] Use of a new module (pandas)
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [ ] A many-to-many relationship in your database structure
- [X] At least one form in your Flask application
- [X] Templating in your Flask application
- [X] Inclusion of JavaScript files in the application
- [X] Links in the views of Flask application page/s
- [X] Relevant use of `itertools` and/or `collections` (generator used in pandas to iterate through dataset)
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [X] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [X] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [X] I included a summary of my project and how I thought it went **in my Canvas submission**!
