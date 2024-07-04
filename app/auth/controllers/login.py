
import datetime
from flask import abort,jsonify,session,make_response,request
from flask_restful import Resource
from werkzeug.security import  generate_password_hash,check_password_hash
from app.models.models import User
from app.serde.serde import UserSchema
import jwt
from app import db,app

class Login(Resource):
    def get(Self):
        return {"login":"Successfull"}

    def post(self):  
        credentials=request.get_json()
        print(credentials)
        if credentials.get("email"):
            user=User.query.filter_by(email=credentials["email"]).first()
        else:
            user=User.query.filter_by(phone=credentials["phone"]).first()

    
        if not user:
            abort(401)

        if not user.verify_password(credentials["password"]):
            
            abort(401)

        db.session.add(user)
        db.session.commit()

        # Retrieve and reuse active session id if user is a service account.
        session['user_id']=user.id

        
        
        payload = {"user": UserSchema().dump(user), 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=10)}
        token = jwt.encode(payload, app.config['SECRET_KEY'],algorithm="HS256")

        response = make_response(token)
        response.set_cookie(
            "currentUser", token, secure=app.config.get("SECURE_COOKIE")
        )

        return response

        
