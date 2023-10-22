#!/usr/bin/python3
"""display “n is a number” only if n is an integer"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """class returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """class returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ciscool(text):
    """display “C ” then the value of the text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display “Python ”, then the value of the text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return ("{:d} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
