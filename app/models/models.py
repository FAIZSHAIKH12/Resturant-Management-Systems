from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "user"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),unique=True)
    _password = db.Column(db.String(255),nullable=False)
    phone=db.Column(db.String(20))
    address=db.Column(db.String(200),nullable=False)
    is_admin=db.Column(db.Boolean,default=False)
    
    order = db.relationship('Order', backref='user', lazy=True, cascade='all, delete-orphan, delete, save-update')

    @property
    def password(self):
        """Reading the plaintext password value is not possible or allowed."""
        raise AttributeError("cannot read password")

    @password.setter
    def password(self, password):
        """
        Intercept writes to the `password` attribute and hash the given
        password value.
        """
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Accept a password and hash the value while comparing the hashed
        value to the password hash contained in the database.
        """

        return check_password_hash(self._password, password)

class Order(db.Model):
    __tablename__ = "order"
    id=db.Column(db.Integer,primary_key=True)
    customer_name=db.Column(db.String(60),nullable=False)
    items_order=db.Column(db.String(60),nullable=False)
    order_id=db.Column(db.Integer)
    total_price=db.Column(db.Float,nullable=False)
    customer_id=db.Column(db.Integer,db.ForeignKey('user.id',ondelete='CASCADE',onupdate='CASCADE'))
    menu_id=db.Column(db.String(50),nullable=False)
    quantity=db.Column(db.String(50),nullable=False)


    

class MenuItem(db.Model):
    __tablename__ = "menu_item"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(70))
    desc=db.Column(db.String(200),nullable=False)
    price=db.Column(db.Integer,nullable=False)
    availability = db.Column(db.Boolean, default=True)

