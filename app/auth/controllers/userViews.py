from flask_restful import Resource
from flask import request
import marshmallow
from app.models.models import User
from app import db

class UserView(Resource):

    def post(self):
        data = User(unknown=marshmallow.EXCLUDE).loads(request.get_json())
        db.session.add(data)
        db.session.commit
        return str("msg: add successfully")