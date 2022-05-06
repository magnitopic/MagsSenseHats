from flask import Flask, render_template, jsonify, redirect
from flask.wrappers import Response
import os
from functions import getInfo, getNames

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template("index.html", names=getNames())


@app.route("/<name>", methods=["GET"])
def userData(name):
    if name not in getNames():
        return redirect("/")
    pyload=getInfo(name)
    pyload["name"]=name
    
    return render_template("information.html", pyload=pyload)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
