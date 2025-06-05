from flask import Flask, request, jsonify, render_template, redirect, url_for
import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    roles = ['admin', 'user', 'guest']
    numbers = [1, 2, 3, 4, 5]
    random_role = random.choice(roles)
    return render_template('index.html', current_time=current_time, user=random_role, numbers=numbers)

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

@app.route('/note_created/<note>')
def note_created(note):
    return render_template('note_created.html', title=note)

@app.route("/create-note", methods=["GET",'POST'])
def create_note():
    if request.method == 'POST':
        note = request.form.get('title', "No title provided")
        if not note:
            return 'Title is required', 400
        return redirect(url_for('note_created',note=note))
    else:
        return render_template('notes_form.html', title="Create Note")


if __name__ == '__main__':
    app.run(debug=True)