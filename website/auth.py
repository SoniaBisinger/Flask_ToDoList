from flask import Blueprint, render_template

#Blueprint : a file with roots

auth = Blueprint('auth', __name__)

#login
@auth.route('/login')
def login():
    #return an HTML Page
    return render_template("login.html", text="Welcome to my website")

#logout

@auth.route('/logout')
def logout():
    return "<p>LogOut</p>"

#signup
@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")
