from sqlalchemy import false
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(50),unique=True)
    password_hash = db.Column(db.String(200))
    user_products = db.relationship('Product',backref = 'user',lazy = "dynamic")

    

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'



class Product(db.Model):
    #properties 
    __tablename__ = 'products'
    product_id = db.Column(db.Integer,primary_key = True)
    product_name = db.Column(db.String(255))
    product_price = db.Column(db.Integer)
    product_desc = db.Column(db.String(255))
    product_img_path = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_products(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_products(cls,id):
        products = Product.query.filter_by(product_id=id).all()
        return products

    def __repr__(self):
        return f'Product {self.product_name}'










