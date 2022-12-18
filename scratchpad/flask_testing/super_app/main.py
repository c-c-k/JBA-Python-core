#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Flask test app: Super App"""

from flask import Flask
from flask import jsonify
from flask import make_response, request
from flask import render_template

app = Flask('super-app')


@app.route('/')
def index():
    response = ("Index page, All good", 200)
    return response


@app.route('/str/<int:val1>/<val2>')
@app.route('/flt/<float:val1>/<int:val2>')
@app.route('/int/<int:val1>/<float:val2>')
def mult(val1, val2):
    print(type(val1))
    return (
        f'{val1} * {val2} = {val1 * val2}'
    )


@app.route('/request_test', methods=['GET', 'POST'])
def request_test():
    method = request.method
    args = request.args
    response = render_template('request_test.html', method=method, args=args)
    return response


@app.route('/err_demo')
def error_page():
    response = make_response('Error page', 404)
    return response


@app.route('/jsonify_demo')
def jsonify_demo():
    data = {
        'id': 45,
        'name': 'test_name',
        'dict': {'key1': 'a', 'key2': 'b'},
        'list': [1, 2, 3],
        'tuple': ('a', 'b'),
    }
    response = jsonify(data)
    response.status_code = 212
    return response


def main():
    app.run()


if __name__ == '__main__':
    main()
