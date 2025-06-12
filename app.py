from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import random
app = Flask(__name__)
import os

DB_FILE_PATH = os.path.join(os.path.dirname(__file__), 'notes.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'

@app.route('/')
def index():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    roles = ['admin', 'user', 'guest']
    notes = Note.query.all()
    numbers = [1, 2, 3, 4, 5]
    random_role = random.choice(roles)
    return render_template('index.html', current_time=current_time, user=random_role, numbers=numbers, notes=notes)

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/about')
def about():
    return 'This is the about notes.'
@app.route('/contact', methods=['GET', 'POST'])
def contact(): 
    if request.method == 'POST':
        return 'Thank you for your message!', 201
    elif request.method == 'GET':   
        return 'This is the contact page.', 200
    elif request.method != 'GET' and request.method != 'POST':
        return 'Method not allowed', 405
    else:
        return 'Invalid request', 400

@app.route("/api/info")
def api_info():
    data = {"version": "1.0", "author": "Blass"}
    return jsonify(data)

@app.route('/page')
def page():
    return '<h1>This is a new page.</h1>'

@app.route('/note_created/<title_note>/<content_note>')
def note_created(title_note, content_note):
    return render_template('note_created.html', title=title_note, content=content_note)

@app.route("/create-note", methods=["GET",'POST'])
def create_note():
    if request.method == 'POST':
        note_title = request.form.get('title', "No title provided")
        note_content = request.form.get('content', "No content provided")
        if not note_title:
            return 'Title is required', 400
        if not note_content:
            return 'Content is required', 400
        note_db = Note(title=note_title, content=note_content)
        db.session.add(note_db)
        db.session.commit()
        return redirect(url_for('note_created',title_note=note_db.title,content_note=note_db.content))
    else:
        return render_template('notes_form.html', title="Create Note")

@app.route("/edit-note/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST': 
        note.title = request.form.get('title', note.title)
        note.content = request.form.get('content', note.content)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('edit_notes_form.html', note=note)
@app.route("/delete-note/<int:note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        db.session.delete(note)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('delete_note.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)