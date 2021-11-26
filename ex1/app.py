from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # call: http://127.0.0.1:5000/?name=Alex
    # #, name=request.args.get("name", "world"))  # GET /search?q=cats ....whatever after ?
    # world is default value

    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))

@app.route("/secret")
def secret():
    return "al"

@app.route("/greet", methods=["POST"])  # need to override get with POST
def greet():
    return render_template("greet.html", name=request.form.get("name", "world")) #name=request.args.get("name", "world"))