from flask import Flask, flash
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']

    #Save(Create New User)
    @classmethod
    def save_new_user(cls,data):
        query='''INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'''
        return connectToMySQL('golf_schema').query_db(query,data)

    #Get All Users
    @classmethod
    def get_all_users(cls):
        query = '''SELECT * FROM users'''
        result = connectToMySQL('golf_schema').query_db(query)
        users = []
        for user in result:
            users.append(cls(user))
        return users
    
    #Get User and Their Favorites
    @classmethod
    def users_with_favorites(cls):
        pass
    
    #Update
    @classmethod
    def update_user(cls,data):
        pass
    
    #Get By Email
    @classmethod
    def get_by_email(cls,data):
        query = """ SELET * FROM users WHERE email = %(email)s"""
        results = connectToMySQL('golf_schema').query_db(query, data)
        if results < 1:
            return False
        return cls(results[0])
    
    #Get By ID
    @classmethod
    def get_by_id(cls,data):
        pass
    
    #Validate User
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len (user['first_name']) < 3:
            flash ("First Name must be at least 3 characters.")
            is_valid = False
        if len (user['last_name']) < 3:
            flash ("Last Name must be at least 3 characters.")
            is_valid = False
        if len (user['password']) < 8:
            flash ("Password must be at least 8 characters.")
        return is_valid