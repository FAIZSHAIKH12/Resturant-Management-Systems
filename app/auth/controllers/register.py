from app.models.models import User
from app.serde.serde import UserSchema
from flask_restful import Resource
import marshmallow
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Register(Resource):
    def get(self):
        data = User.query.all()
        return UserSchema(many=True).dump(data)
        
    def post(self):
        data = UserSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        if data:
            user = User(**data)
            db.session.add(user)
            db.session.commit()
        else:
            raise ValueError("json is not valid")

        return UserSchema().dump(data)

        
    
    

    
    
    

    
    
