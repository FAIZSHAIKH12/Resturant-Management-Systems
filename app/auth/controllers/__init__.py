from flask_restful import Api
from flask import Blueprint

from app.auth.controllers.login import Login
from  app.auth.controllers.register import Register

auth_blueprint = Blueprint("auth",__name__,url_prefix="/auth")


api = Api(auth_blueprint)

api.add_resource(Login,"/login/")
api.add_resource(Register,"/register/")