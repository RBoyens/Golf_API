from flask import Flask, render_template,request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

@app.route("/")
def Login ():
    return render_template('login.html')

@app.route("/register", methods=['POST']) 
def register_user():
    if not User.validate_user(request.form):
        return redirect('/')
    
    if request.form['password'] !=request.form['confirm_password']:
        flash("Passwords do not match!")
        return redirect ('/')
    data ={
        "email": request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if user_in_db:
        flash('Email already exists')
        return redirect ('/')
    pw_hash = Bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "passwords":pw_hash
    }
    user_id = User.save_new_user(data)
    session['id'] = user_id
    return redirect ('/dashboard')