from flask import Flask, render_template
from flask_app import app

@app.route("/dashboard")
def Home ():
    return render_template('dashboard.html')

@app.route("/dashboard/details")
def Detail ():
    return render_template('detail.html')