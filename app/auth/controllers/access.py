
from flask_restful import Resource
from app.auth.decorators import require_login

class Access(Resource):
    method_decorators= [require_login]