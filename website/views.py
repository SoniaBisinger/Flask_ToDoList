from flask import Blueprint, render_template

#Blueprint : a file with roots

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
