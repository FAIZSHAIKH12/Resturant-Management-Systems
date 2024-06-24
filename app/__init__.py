from flask import Flask
from flask_sqlalchemy  import SQLAlchemy



db=SQLAlchemy()



def create_app():
    global app
    app=Flask(__name__)
    app.config['SECRET_KEY']='mccramaf'
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost:5050/resturant_mgm'
    db.init_app(app)
  
    from app.auth.controllers import auth_blueprint

    app.register_blueprint(auth_blueprint,
                           url_prefix=f'/api/{auth_blueprint.url_prefix}')

    return app

