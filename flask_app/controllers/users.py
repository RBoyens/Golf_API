from flask import Flask, render_template,request, redirect, flash, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/")
def index ():
    return redirect('/home')

@app.route('/home')
def Login ():
    return render_template('login.html')

@app.route('/register', methods=['POST']) 
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
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":pw_hash
    }
    user_id = User.save_new_user(data)
    session['id'] = user_id
    return redirect ('/dashboard')

@app.route("/login", methods=['POST'])
def login_user():
    data ={
        "email":request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email or Password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')
    session['id'] = user_in_db
    return redirect ('/dashboard')

@app.route('/logout')
def logout():
    session.clear
    redirect('/')
