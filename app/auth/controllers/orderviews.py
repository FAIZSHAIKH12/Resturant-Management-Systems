# from flask_restful import Resource
from flask import jsonify, request,g
import marshmallow
from app.models.models import Order,MenuItem
from app import db
from app.serde.serde import OrderSchema
from app.auth.controllers.access import Access
from datetime import datetime

class OrderView(Access):
    def get(self):
        data = Order.query.filter_by(customer_id=g.user.id).all()
        # id=0
        for d in range(len(data)):
            data[d].items_order=data[d].items_order.split(",")
        return OrderSchema(many=True).dump(data)
    


    def post (self):
        data = OrderSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        items = list(data["items_order"])
        
        quantity = list(data["quantity"])
        if len(items) == len(quantity):
            ord_item=[]
            for item in items:
                it = MenuItem.query.filter_by(name=item).first()

                if not it:
                    return f"{items} is not in our MenuList"
                ord_item.append((it.id,it.price,item))                   
            orders =  Order.query.all()
            order_id = len(orders)+1
            total_amount = 0
            menu_id =""
            ordered_items=''
            for i in range(len(ord_item)):
                menu_id += str(ord_item[i][0])+", "
                t_price = int(quantity[i]) * ord_item[i][1]
                total_amount += t_price
                ordered_items+= ord_item[i][2]+", "
            user_g=g.user
            data['customer_name']=user_g.name
            data['customer_id']=user_g.id
            data['total_price'] = total_amount
            data['menu_id'] = menu_id
            data['items_order']=ordered_items
            data['quantity'] = " ".join(quantity)
            user = Order(**data,order_id=order_id)
            db.session.add(user)
            db.session.commit()

            quantity_and_items = []
          
            for i in range(len(items)):
                quantity_and_items.append((items[i], quantity[i]))
            
            return jsonify({"msg":f"product ordered at {datetime.now()} we will deliver within 30 minutes",
                            "orders":{"customer_name":user_g.name,"order_id":order_id,"items and quantity":quantity_and_items,
                            "total_price":total_amount}})
        else:
            return jsonify({"msg":"items and quantity are mismatch"})
        

    def put(self):
        data = OrderSchema(unknown=marshmallow.EXCLUDE).load(request.get_json())
        try:
            orders = Order.query.filter_by(order_id=data["order_id"]).first()
            if orders:
                if len(data["items_order"]) != len(data["quantity"]):
                    raise ValueError("quantiy and items should be equal")
                if orders.total_price != data["total_price"]:
                    raise ValueError("you cannot change amount")
                if orders.order_id != data["order_id"]:
                    raise ValueError("you cannot change order id")
                if orders.customer_id != g.user.id:
                    raise ValueError("you cannot change customers id")
                if orders.menu_id != data["menu_id"]:
                    raise ValueError("you cannot change menuid")
                menu_id = orders.menu_id
                amount=[]
                for id in menu_id:
                    am=MenuItem.query.filter_by(id=int(id)).first()
                    amount.append(am.price)
                total_amount=0
                
                for i in range(len(data["quantity"])):
                    total_amount += amount[i]*int(data["quantity"][i])
                print(total_amount)
                orders.quantity=" ".join(data["quantity"])
                orders.total_price=total_amount
                db.session.commit()

                return "success"
            else:
                return {"msg":"please check order id"}
        except Exception as e:
            print(e)
    

    def delete(self,order_id):
        data=Order.query.filter_by(order_id=order_id).first()
        db.session.delete(data)
        db.session.commit()
        return "order delete successfully",201
