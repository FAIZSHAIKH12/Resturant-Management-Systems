from flask_restful import Resource
from flask import jsonify, request,session,g
import marshmallow
from app.auth.controllers.access import Access
from app.auth.decorators import grant_permission
from app.models.models import User
from app import db
from app.serde.serde import UserSchema

class ShowView(Access):
    def post(self):
        data = UserSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        menu = User(**data)
        db.session.add(menu)
        db.session.commit()
        return UserSchema().dump(data)
       

    @grant_permission
    def get(self,id=None):
        if not id:
            user=User.query.all()
            return UserSchema(many=True).dump(user)
        data=User.query.filter_by(id=id).first()
        return UserSchema().dump(data)
    


    def put(self):
     
        data = UserSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())

        user = User.query.filter_by(id=g.user.id).first()
        if user:
            try:
                for key,value in data.items():
                    setattr(user,key,value)
                db.session.commit()
                return "success"
            except Exception as e:
                print(e)
                return {"msg": "error updating data"}
        else:
            return {"msg": "no existing data"}
        
       

        
        

    

     
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return "delete"


