from os import name
from flask import Flask, redirect, render_template, request, session # session is a global variable
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # remember user logged in
        # redirect to /

        # store the name in a session
        session["name"] = request.form.get("name") # use as a dict
        return redirect("/")


    return render_template("login.html")

@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")