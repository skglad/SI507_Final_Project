import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import re


# App configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./books.db_project_final' # database name
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app)
session = db.session

#########
######### Everything above this line is set-up.
#########



#setting up models - using db.Model rather than base
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    rating = db.Column(db.Float)
    image_link = db.Column(db.String)
    year_published = db.Column(db.Integer)
    #author = db.Column(db.relationship('Author',backref='books'))

    def __repr__(self):
        return "{} by {}".format(self.title, self.author.name)


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship("Book", backref = "author")

    def __repr__(self):
        return "{}".format(self.title)


### Function from example that help with database creation

def get_or_create_author(author_name):
    author = Author.query.filter_by(name=author_name).first()
    if author:
        return author
    else:
        author = Author(name=author_name)
        session.add(author)
        session.commit()
        return author

#function to create a new book (does not allow duplicate titles)
def new_book_input(row):
    if Book.query.filter_by(title= row['original_title']).first():
        return "</h2>Sorry that book is already in the database.</h2>"
    else:
        author = get_or_create_author(row['authors'])
        book = Book(title = row['original_title'], author_id=author.id, rating = row['average_rating'], image_link = row['image_url'], year_published = row['original_publication_year'] )
        session.add(book)
        session.commit()
        return "<h2>New book added!"

###routes for flask application

# App routes (minimum of 3)
@app.route('/')
def welcome():
    return render_template('background.html')
    #return render_template('test.html')
    #return " <h2>There are {} books in this database.<br> There are {} authors in this database.".format(num_books, num_author)

#route to get information about the database
@app.route('/information')
def index():
    books = Book.query.all()
    num_books = len(books)
    authors = Author.query.all()
    num_author = len(authors)
    return render_template('information.html')
    #return " <h2>There are {} books in this database.<br> There are {} authors in this database.</h2>".format(num_books, num_author)


#route with form to return list of books by a specific author
@app.route('/author')
def author_form():
    return render_template('author-form.html')

@app.route('/author', methods=['POST'])
def author_form_post():
    author = request.form['text']
    #author = text.title()
    #book_list = Author.query.filter_by(name=author).first().books
    try:
        book_list = Author.query.filter(Author.name.ilike(author)).first().books
        return render_template("author-list.html", book_list = book_list)
    except AttributeError:
        #return "Sorry, no titles by {} exist. Please check your spelling and try again.".format(text)
        return render_template('author-list.html')


#route with form to return book titles with a specific search term
@app.route('/search')
def search_form():
    return render_template('search-form.html')

@app.route('/search', methods=['POST'])
def search_form_post():
    search = request.form['text']
    title_list = Book.query.filter(Book.title.contains(search)).all()
    #title_list = Book.query.filter(Book.title.op('regexp')(r'\b{}\b'.format(search))).all()
    #return "{}".format(book_list)
    return render_template ('search-return.html', title_list = title_list)


#route with form that returns image of the book
@app.route('/bookcover')
def cover_form():
    return render_template('cover-form.html')

@app.route('/bookcover', methods=['POST'])
def cover_form_post():
    title = request.form['text']
    #search = str(text)
    book_image = Book.query.filter(Book.title.ilike(title)).all()
    return render_template ('image.html', book_image = book_image)
    #return render_template ('test.html', title_list = title_list)


# ###insert data###
@app.before_first_request
def insert_data():
    books_df = pd.read_csv('books_clean.csv') #pandas module
    books_df = books_df.iloc[:2000]
    for index, row in books_df.iterrows(): #use of generator
        new_book_input(row)


if __name__ == '__main__':
    db.create_all()
    app.run()
