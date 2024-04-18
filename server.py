from flask_app import app
# be sure to import flask_app.controller so the routes will work
from flask_app.controllers import users

if __name__ == '__main__':
    app.run(debug=True)