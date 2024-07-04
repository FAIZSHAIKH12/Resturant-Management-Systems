from functools import wraps
from flask import jsonify,request,session,g
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
            g.user=current_user
        except:
            return jsonify({'message' : 'Token is  not valid!'})
        return func(*args, **kwargs)
    return decorated



def grant_permission(a):
    @wraps(a)
    def decorator(*args,**kwargs):
        token=request.cookies.get('currentUser')
        if not token:
            return str("msg:token expired"),401
        secret_key=str(app.config['SECRET_KEY'])
        try:
            user_data=jwt.decode(token,secret_key,algorithms=['HS256'])
            user =User.query.filter_by(id=user_data['user']['id']).first()
        except:
            pass
        if user.is_admin == True:
            return a(*args,**kwargs)
        else:
            return "permission denied"
    return decorator
    
    

        

         