#!/usr/bin/python3


from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    strict_slashes = False
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    strict_slashes = False
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    strict_slashes = False
    return text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    strict_slashes = False
    return "Python " + text.replace("_", " ")

app.run(host="0.0.0.0", port=5000)
