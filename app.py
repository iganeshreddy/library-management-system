from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import BookForm
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, year=form.year.data)
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for('home'))
    return render_template('add_book.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.year = form.year.data
        db.session.commit()
        flash("Book updated successfully!", "success")
        return redirect(url_for('home'))
    return render_template('edit_book.html', form=form, book=book)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash("Book deleted successfully!", "danger")
    return redirect(url_for('home'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = Book.query.filter(Book.title.ilike(f'%{search_term}%')).all()
        return render_template('search.html', results=results, search_term=search_term)
    return render_template('search.html', results=None)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
