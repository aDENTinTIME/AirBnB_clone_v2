#!/usr/bin/python3


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

if __name__ == "__main__":
    @app.route("/")
    def hello():
        return "Hello HBNB!"

    @app.route("/hbnb")
    def hbnb():
        return "HBNB"

    @app.route("/c/<text>")
    def c_text(text):
        return text.replace("_", " ")

    @app.route("/python/")
    @app.route("/python/<text>")
    def python_text(text="is cool"):
        return "Python " + text.replace("_", " ")

    @app.route("/number/<int:n>")
    def number_text(n):
        return "{} is a number".format(n)

    @app.route("/number_template/<int:n>")
    def number_template(n):
        return render_template("5-number.html", number=n)

    app.run(host="0.0.0.0", port=5000)
