#make the folder 'website' a python package
from flask import Flask

#initialize a flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Kira & Nala'

    #tell we have blueprints (import this file)
    from .views import views
    from .auth import auth

    #register blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
