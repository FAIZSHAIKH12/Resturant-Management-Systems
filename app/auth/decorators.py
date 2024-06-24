from functools import wraps
from flask import jsonify,request,session
import jwt
from app.models.models import User
from app import app


def require_login(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        token=request.cookies.get('currentUser')

        
        if not token:
            return jsonify({'message' : 'Token is missing!'})
        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"],options=None)
            current_user = User.query.filter_by(id=data["user"]["id"]).first()
            if current_user.id != session["user_id"]:
                return jsonify({'message' : 'Token is  not valid!'})
        except:
            return jsonify({'message' : 'Token is  not valid!'})

        return func(*args, **kwargs)
    return decorated

        

         