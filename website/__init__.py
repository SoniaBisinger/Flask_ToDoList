#make the folder 'website' a python package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize our DB
db = SQLAlchemy()
DB_NAME = "database.db"

#initialize a flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Kira & Nala'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #tell we have blueprints (import this file)
    from .views import views
    from .auth import auth

    #register blueprint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
