from flask import Flask, render_template, Blueprint, redirect, request
from models.book import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository
from models.author import Author

books_blueprint = Blueprint("books", __name__)



# INDEX
# GET '/books'
@books_blueprint.route("/books")
def get_books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

# NEW
# GET '/books/new'
@books_blueprint.route("/books/new", methods=["GET"])
def new_task():
    return render_template('books/new.html')


# CREATE
# POST '/books'
@books_blueprint.route("/books", methods = ['POST'])
def add_book_a():
    first_name = request.form ['first_name']
    last_name = request.form ['last_name']

    author = Author(first_name, last_name)
    author_repository.save(author)

    title = request.form['title']
    genre = request.form['genre']
    publisher = request.form['publisher']

    book = Book(title, genre, publisher, author)

    book_repository.save(book)
    return redirect('/books')

    



# SHOW
# GET '/books/<id>'


# EDIT
# GET '/books/<id>/edit'


# UPDATE
# PUT '/books/<id>'



# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_books(id):
    book_repository.delete(id)
    return redirect('/books')


