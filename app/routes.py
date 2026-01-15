from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1.html')
def ejercicio1():
    return render_template('ejercicio1.html')