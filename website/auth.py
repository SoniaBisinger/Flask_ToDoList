from flask import Blueprint

#Blueprint : a file with roots

auth = Blueprint('auth', __name__)

#login
@auth.route('/login')
def login():
    #return an HTML Page
    return "<p>LogIn</p>"

#logout

@auth.route('/logout')
def logout():
    return "<p>LogOut</p>"

#signup
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
