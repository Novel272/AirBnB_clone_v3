#!/usr/bin/python3
""" 4. Adds a 4th view func that display var only if integer """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Return a type text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Returns text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text to variables. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replaces text with val. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace by int if given int. """
    n = str(n)
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
