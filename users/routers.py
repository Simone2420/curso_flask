from flask import render_template, request, redirect, url_for,Blueprint, flash, session
from models import User, db
users_bp = Blueprint("users", __name__)

@users_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash("User registered sucessfuly", "success")
        return redirect(url_for("users.login"))
    else:
        return render_template("users_register_form.html")

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(username=username, email=email, password=password).first()
        if user:
            session["user_id"] = user.id
            session["username"] = user.username
            session["email"] = user.email
            flash("Login successful", "success")
            return redirect(url_for("users.dashboard", username=user.username,email=user.email))
        else:
            return "Invalid username, email or password"
        
    else:
        return render_template("users_login.html")

@users_bp.route("/dashboard/<username>/<email>", methods=["GET", "POST"])
def dashboard(username,email):
    return render_template("user_dashboard.html",username=username,email=email)

@users_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("email", None)
    flash("You have been logged out", "success")
    print(session)
    return redirect(url_for("users.login"))