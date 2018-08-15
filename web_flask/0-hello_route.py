#!/usr/bin/python3


app = Flask(__name__)


if __name__ == "__main__":
    @app.route("/")
    def hello():
        strict_slashes = False
        return "Hello HBNB!"

    app.run(host="0.0.0.0", port=5000)
