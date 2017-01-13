from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)



'''Application home page. Shows current unread books.'''

@app.route('/')
def home_page():
    return redirect(url_for('show_books', read='UNREAD'))


@app.route('/add', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        pass
        #add book
        book = Book('bork', 'tilley', 3)
        return redirect(url_for(book_info, book_id=3))

    else:
        #show add book form
        return render_template('add_book.html')


@app.route('/book/<int:book_id>')
def book_info(book_id):
    #show data about one book

    book = {'title':'bork', 'author':'tilley', 'book_id':3, 'read':True }
    return render_template('book.html', book=book)


# URL?
@app.route('/book/read', methods=['POST'])
def book_read():
    #Update database
    #Was book read or not? this could be used to make read book as unread.

    print(request.form)
    read = request.form['read']
    book_id = request.form['book_id']
    #update db

    print(read)
    print(book_id)


    return redirect(url_for('book_info', book_id=book_id))


@app.route('/booklist/<read>')
def show_books(read):

    booklist = [ {'title':'bork', 'author':'tilley', 'book_id':3, 'read':True } , {'title':'spork', 'author':'clara', 'book_id':4, 'read':False }]

    if read == 'READ':
        #show read books
        pass

    elif read == 'UNREAD':
        pass
        #Show unread

    else:
        #show all
        pass

    return render_template('booklist.html', booklist=booklist)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404
