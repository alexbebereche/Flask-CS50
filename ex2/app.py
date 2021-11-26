from flask import Flask, render_template, request, redirect
from cs50 import SQL
# from flask_mail import Mail, Message
# import os


app = Flask(__name__)


# REGISTRANTS = {}

db = SQL("sqlite:///example.db")


SPORTS = [
    "Dodgeball",
    "Football",
    "Basketball",
    "Volleyball"
]
cur = None

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)  # Flask requires to choose a name

@app.route("/register", methods=["POST"]) # dont forget to specify POST
def register():
    # if not request.form.get("name") or request.form.get("sport") not in SPORTS: # validating submissions, dont trust user input
    #     return render_template("failure.html")
    # return render_template("succes.html")

    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    # return render_template("registrants.html", registrants=REGISTRANTS)

    db.execute("INSERT INTO Registrants (name, sport) VALUES(?, ?)", name, sport)


    return redirect("/registrants")
    # return render_template("succes.html")


@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT * FROM Registrants") # getting back rows, dict of cols and values
    return render_template("registrants.html", registrants=rows)

if __name__ == "__main__":
    app.run(debug=True)