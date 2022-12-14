#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Flask test app: Super App'''

from flask import Flask
from flask import request
from flask import render_template

app = Flask('super-app')


@app.route('/')
def index():
    return 'Flask Hellow World'


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
    if request.method == 'GET':
        page = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>request test</title>
  </head>
  <body>
    <div>
      <form method="post">
        <input type="text" name="text_input">
        <input type="checkbox" name="cb_input">
        <input type="submit" name="sub">
      </form>
    </div>
    <hr>
    <div>
      <form method="get">
        <input type="search" name="search_input">
      </form>
    </div>
  </body>
</html>
        """
        page += f"<p> GET args are: {str(request.args)}</p>"
        return page
    elif request.method == 'POST':
        page = f"<p> POST args are: {str(request.data)}</p>"
        return page

def main():
    app.run()


if __name__ == '__main__':
    main()
