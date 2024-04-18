from flask import Flask, render_template
from flask_app import app

@app.route("/")
def Login ():
    return render_template('login.html')