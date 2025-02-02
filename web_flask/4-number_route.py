#!/usr/bin/python3
""" script that starts a Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number" .format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
