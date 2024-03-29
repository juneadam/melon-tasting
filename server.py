# Flask routing for melon-tasting app

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from passlib.hash import argon2
from jinja2 import StrictUndefined
from random import choice, randint, shuffle
from model import connect_to_db, db
# import crud

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_homepage():
    """Render the HTML template for the app."""

    return render_template('base.html')

@app.route('/login-check.json')
def login_check():

    if not session.get('user_id'):
        return jsonify({'data': 0})
    else:
        return jsonify({'data': 1})

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)