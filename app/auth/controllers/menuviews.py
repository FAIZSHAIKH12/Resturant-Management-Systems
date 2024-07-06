from flask_restful import Resource
from flask import jsonify, request,session
import marshmallow
from app.auth.controllers.access import Access
from app.auth.decorators import grant_permission
from app.models.models import MenuItem
from app import db
from app.serde.serde import MenuItemSchema

class PostView(Access):
    @grant_permission
    def post(self):
        data = MenuItemSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        menu = MenuItem(**data)
        db.session.add(menu)
        db.session.commit()
        return MenuItemSchema().dump(data),201
    
    def get(self):
        data=MenuItem.query.all()
        return MenuItemSchema(many=True).dump(data)



class MenuView(Access):

    def get(self,name):
        data=MenuItem.query.filter_by(name=name).first()
        return MenuItemSchema().dump(data)
    


    def put(self,id):
        item = MenuItem.query.get(id)
        if not item:
            return jsonify({"error": "MenuItem not found"}), 404
        
        data = request.get_json()

        if 'name' in data:
            item.name = data['name']
        if 'desc' in data:
            item.desc = data['desc']
        if 'price' in data:
            item.price = data['price']
        if 'availability' in data:
            item.availability = data['availability']
        
        db.session.commit()
        return jsonify({
            "message": "MenuItem updated successfully", 
            "menu_item": {
                "id": item.id,
                "name": item.name,
                "desc": item.desc,
                "price": item.price,
                "availability": item.availability
            }
        }),201



    def delete(self,id):
        data=MenuItem.query.filter_by(id=id).first()
        db.session.delete(data)
        db.session.commit()
        return "delete"


    
 
    
    




    

