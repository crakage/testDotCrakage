from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template(url_for('index.html'))


@app.route('/login')
def login():
    redirect(url_for('index'))

