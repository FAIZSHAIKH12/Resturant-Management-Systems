from flask_restful import Api
from flask import Blueprint

from app.auth.controllers.login import Login
from app.auth.controllers.menuviews import MenuView
from app.auth.controllers.orderviews import OrderView
from  app.auth.controllers.register import Register
from app.auth.controllers.menuviews import PostView

from app.auth.controllers.userviews import UserView
from app.auth.controllers.userviews import ShowView



auth_blueprint = Blueprint("auth",__name__,url_prefix="/auth")


api = Api(auth_blueprint)

#api for authenticate and authorization for user.
api.add_resource(Login,"/login")
api.add_resource(Register,"/register")


#api for CRUD operation on MENUITEMS TABLES.
api.add_resource(MenuView,"/get/<name>")
api.add_resource(PostView,"/add")


#api for CRUD on USER TABLES.
api.add_resource(UserView,"/user/<int:id>")
api.add_resource(ShowView,"/user")

#api for crud on order tables.
api.add_resource(OrderView,"/order/","/order/<int:order_id>")
# api.add_resource(OrderView,)




