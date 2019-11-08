# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:56:37 2019

@author: luisa
"""

from flask import Flask

app= Flask(__name__)
@app.route('/')


def index():
    return "olaaaa seus boboes"

if __name__ =="__main__":
    app.run(debug=True)
    

user = {'username': 'Miguel'}

#from app import app

from flask import Flask

app= Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''