from flask_restful import Resource
from flask import jsonify, request,session
import marshmallow
from app.models.models import MenuItem
from app import db
from app.serde.serde import MenuItemSchema

class MenuView(Resource):

    def post(self):
        data = MenuItemSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        menu = MenuItem(**data)
        db.session.add(menu)
        db.session.commit()
        return MenuItemSchema().dump(data)
    
    def get(self):
        data=MenuItem.query.all()
        schema=MenuItemSchema(many=True)
        return schema.dump(data)

    
