from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for

bp = Blueprint("root", __name__)
app = Flask(__bookstore__)
ooks = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 10.99},
    {"id": 2, "title": "1984", "author": "George Orwell", "price": 8.99},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 12.99},
]

@app.route('/')
def home():
    return render_template('home.html', books=books)


@bp.route("/")
def index():
    app.logger.warning("sample message")
    return render_template("index.html")

app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return "Book not found", 404
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)