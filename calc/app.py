# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = add(a, b)
    return f'The result of {a} + {b} is: {result}'

@app.route('/sub')
def subtraction():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    result = sub(a, b)
    return f'The result of {a} - {b} is: {result}'

@app.route('/mult')
def multiplication():
    a = float(request.args.get('a', 1))
    b = float(request.args.get('b', 1))
    result = mult(a, b)
    return f'The result of {a} * {b} is: {result}'

@app.route('/div')
def division():
    a = float(request.args.get('a', 1))
    b = float(request.args.get('b', 1))

    if b == 0:
        return 'Error: Division by zero is undefined.'

    result = div(a, b)
    return f'The result of {a} / {b} is: {result}'