from flask import Flask, json

import math
# test 32


app = Flask(__name__)


@app.route('/')
def default_route():
    return 'App Calculates Factorial! Give /factorial/number'


@app.route('/factorial/<int:factorial_number>')
def factroial(factorial_number):
    response = app.response_class(
        response=json.dumps(math.factorial(factorial_number)),
        status=200,
        mimetype='application/json'
    )
    return response
