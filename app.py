# Standard library imports

# Third-party imports
from flask import (
    Flask,
    jsonify,
    request,
    render_template
)
from datetime import datetime
import random
from config import Config
from models import Note, db
from notes.routers import notes_bp
from users.routers import users_bp
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()
app.register_blueprint(notes_bp)
app.register_blueprint(users_bp)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    roles = ["admin", "user", "guest"]
    notes = Note.query.all()
    numbers = [1, 2, 3, 4, 5]
    random_role = random.choice(roles)
    return render_template(
        "index.html",
        current_time=current_time,
        user=random_role,
        numbers=numbers,
        notes=notes,
    )
@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"


@app.route("/about")
def about():
    return "This is the about notes."


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Thank you for your message!", 201
    elif request.method == "GET":
        return "This is the contact page.", 200
    elif request.method != "GET" and request.method != "POST":
        return "Method not allowed", 405
    else:
        return "Invalid request", 400


@app.route("/api/info")
def api_info():
    data = {"version": "1.0", "author": "Blass"}
    return jsonify(data)


@app.route("/page")
def page():
    return "<h1>This is a new page.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
