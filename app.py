from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def login():
    return 'this is a test!!!'

