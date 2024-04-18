from flask import Flask
from flask_app import app

@app.route("/")
def index ():
    return "Server is working"