from myapp import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATEBASE = 'database.db'

posts = []



@app.route('/', methods=['GET', 'POST'])
def index():
    con = sqlite3.connect(DATEBASE)
    db_books = con.execute(
        'SELECT id, title, price, arrival_day FROM books'
    ).fetchall()
    con.close()

    books = []
    for row in db_books:
        books.append({
            'id': row[0],
            'title': row[1],
            'price': row[2],
            'arrival_day': row[3],
        })

    if request.method == 'POST':
        question = request.form['question']
        posts.append({
            "question": question,
            "answer": ""
        })
        return redirect('/')

    return render_template('index.html', books=books, posts=posts)


@app.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    con = sqlite3.connect(DATEBASE)
    con.execute('DELETE FROM books WHERE id = ?', [book_id])
    con.commit()
    con.close()
    return redirect(url_for('index'))


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    price = request.form['price']
    arrival_day = request.form['arrival_day']
    
    con = sqlite3.connect(DATEBASE)
    con.execute('INSERT INTO books (title, price, arrival_day) VALUES (?, ?, ?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))

@app.route('/reply/<int:index>', methods=['POST'])
def reply(index):
    answer = request.form['answer']
    posts[index]['answer'] = answer
    return redirect('/')
