from flask_restful import Resource
from flask import jsonify, request,session
import marshmallow
from app.auth.controllers.access import Access
from app.auth.decorators import grant_permission
from app.models.models import User
from app import db
from app.serde.serde import UserSchema


class ShowView(Resource):
    def post(self):
        data = UserSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        menu = User(**data)
        db.session.add(menu)
        db.session.commit()
        return UserSchema().dump(data)
    
    @grant_permission
    def get(self):
        user=User.query.all()
        return UserSchema(many=True).dump(user)



class UserView(Resource):
    @grant_permission
    def get(self,id):
        data=User.query.filter_by(id=id).first()
        return UserSchema().dump(data)
    


    def put(self,id):
        item = User.query.get(id)
        if not item:
            return jsonify({"error": "User not found"}), 404
        data = request.get_json()
        if 'name' in data:
            item.name = data['name']
        if 'email' in data:
            item.desc = data['email']
        if 'phone' in data:
            item.price = data['phone']
        if 'address' in data:
            item.availability = data['address']

        
        db.session.commit()
        return jsonify({
            "message": "User updated successfully", 
            "user": {
                "id": item.id,
                "name": item.name,
                "email": item.email,
                "phone": item.phone,
                "address": item.address
            
            }
        }),201

    
    def delete(self,id):
        data=User.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return  jsonify({"message":"User Deleted Successfully"}),201
