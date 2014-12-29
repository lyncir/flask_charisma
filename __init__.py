# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/error')
def error():
    return render_template('error.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/chart')
def charts():
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
