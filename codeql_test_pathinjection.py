import os.path

from flask import Flask, request

app = Flask(__name__)


def source():
    return request.args.get("path", "")


def normalize(x):
    return os.path.normpath(x)


@app.route("/path")
def simple():
    x = source()
    open("") # not x
