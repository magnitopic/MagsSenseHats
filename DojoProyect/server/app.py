from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
import os
from functions import getInfo

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    pyload = getInfo()
    return render_template("index.html", pyload=pyload)


if __name__ == "__main__":
    app.run(debug=True)
