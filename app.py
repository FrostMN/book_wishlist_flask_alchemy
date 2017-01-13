from flask import Flask
from flask import url_for, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'   # /// relative path to this app.    # //// absolute path to somewhere on file system
db = SQLAlchemy(app)

app.logger.setLevel(10)   ## Todo turn on logging in config file
app.secret_key = 'Change to something random.'# move to config file

from models import *

'''Application home page. Redirects to list of unread books.'''
@app.route('/')
def home_page():
    return redirect(url_for('show_books', read='UNREAD'))


@app.route('/add', methods=['POST', 'GET'])
def add_book():

    if request.method == 'POST':

        author = request.form['author']
        title = request.form['title']

        # Checkboxes don't include any data in the post request if not checked.
        # If there's no data for the 'read' parameter, assume checkbox was not checked.
        if 'read' in request.form:
            read = request.form['read']
        else:
            read = False

        book = Book(author, title, read)

        db.session.add(book)
        db.session.commit()

        return redirect(url_for('book_info', book_id=book.book_id))

    else:
        #A GET request. Show the add book form
        return render_template('add_book.html')



@app.route('/book/<int:book_id>')
def book_info(book_id):
    #show data about one book
    book = Book.query.get_or_404(book_id)           # Raise 404 if book not found.
    return render_template('book.html', book=book)



@app.route('/book/read', methods=['POST'])
def book_read():

    #Was book read or not? this could be used to make read book as unread.

    app.logger.debug(request.form)
    read = request.form['read']
    book_id = request.form['book_id']

    book = Book.query.get(book_id)   # get() function for fetching by primary key.

    if book:
        book.read = read
        db.session.add(book)
        db.session.commit()
        flash('Book updated.')
    else :
        app.logger.error('Book id %s not found in DB' % book_id)
        abort(500)   # Should not be able to make this request. Cancel and return 500 error code.

    return redirect(url_for('book_info', book_id=book_id))


@app.route('/booklist/<read>')
def show_books(read):

    if read == 'READ':
        #show read books
        title = 'Books you\'ve read'
        booklist = Book.query.filter_by(read=True).all()

    elif read == 'UNREAD':
        title = 'Books to read'
        booklist = Book.query.filter_by(read=False).all()

    else:
        title = 'All books'
        booklist = Book.query.all()

    return render_template('booklist.html', title=title, booklist=booklist)


@app.route('/book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return '', 204  # Empty response and no content

    else:
        app.logger.error('Attempting to delete book id %s but it was not found in db. ' % book_id)
        abort(500) # book not found.



@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404
