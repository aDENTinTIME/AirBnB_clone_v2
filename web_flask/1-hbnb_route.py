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

app.run(host="0.0.0.0", port=5000)
