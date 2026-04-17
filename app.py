from flask import Flask, render_template, request, redirect, session
from models import db, User, Appareil, Telescope
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app)

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")
    return redirect("/appareils")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["user_id"] = user.id
            return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/appareils")
def appareils():
    if "user_id" not in session:
        return redirect("/login")
    data = Appareil.query.all()
    return render_template("appareils.html", appareils=data)

@app.route("/telescopes")
def telescopes():
    if "user_id" not in session:
        return redirect("/login")
    data = Telescope.query.all()
    return render_template("telescopes.html", telescopes=data)

@app.route("/photos")
def photos():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("photos.html")

if __name__ == "__main__":
    app.run(debug=True)