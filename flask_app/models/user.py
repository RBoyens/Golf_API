from flask_app.config import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data ['password']

    #Get All Users
    @classmethod
    def get_all_users(cls):
        pass
    
    #Get User and Their Favorites
    @classmethod
    def users_with_favorites(cls):
        pass
    
    #Save(Create New User)
    @classmethod
    def save_new_user(cls,data):
        pass
    
    #Update
    @classmethod
    def update_user(cls,data):
        pass
    
    #Get By Email
    @classmethod
    def get_by_email(cls,data):
        pass
    
    #Get By ID
    @classmethod
    def get_by_id(cls,data):
        pass
    
    #Validate User
    @classmethod
    def validate_user(user):
        pass