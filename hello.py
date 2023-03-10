from flask import Flask, url_for, request, render_template, make_response, abort, redirect, url_for
from markupsafe import escape, Markup
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Index'

@app.route('/profile')
def profile():
    return 'Profile'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

    #$ python -c 'import os; print(os.urandom(16))' generates a secret key