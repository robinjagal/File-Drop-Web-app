from webapp import app
from flask import Flask,render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/makeroom')
def makeRoom():
    return render_template('makeRoom.html')

@app.route('/joinroom')
def joinRoom():
    return render_template('joinRoom.html')