#!/usr/bin/python3


from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False

if __name__ == "__main__":
    @app.teardown_appcontext
        storage.close()

    @app.route("/states_list")
    def states_list():
        return render_template("7-states_list.html", states=storage.all("State"))

    app.run(host="0.0.0.0", port=5000)
