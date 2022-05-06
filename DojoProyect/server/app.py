from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
import os
from functions import getInfo,getNames

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", names=getNames())


if __name__ == "__main__":
    app.run(debug=True)
