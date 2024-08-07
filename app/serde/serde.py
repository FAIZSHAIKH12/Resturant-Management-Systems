from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    id=fields.Int(dump_only=True)
    name = fields.Str(validate=validate.Regexp(r'^[a-zA-Z0-9]+$'))
    phone=fields.Str(validate=validate.Regexp(r'^\d{10}$'))
    address=fields.Str(required=True)
    is_admin=fields.Bool()
    email=fields.Str(required=True)
    password=fields.Str(validate=validate.Regexp(r'^\d{8}$'))


class MenuItemSchema(Schema):
    id=fields.Int(dump_only=True)
    name=fields.Str(required=True)
    desc=fields.Str(required=True)
    price=fields.Int()
    availability = fields.Bool(required=True)

    
class OrderSchema(Schema):
    id=fields.Int(dump_only=True)
    customer_name=fields.Str()
    items_order=fields.List(fields.Str(), required=True)
    order_id=fields.Int()
    total_price=fields.Float()
    customer_id=fields.Int()
    menu_id=fields.Str()
    quantity = fields.List(fields.Str(), required=True)
   


