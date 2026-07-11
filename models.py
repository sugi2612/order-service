from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Order(db.Model):

    __tablename__="orders"

    id=db.Column(db.Integer,primary_key=True)

    user_id=db.Column(db.Integer)

    product=db.Column(db.String(100))

    quantity=db.Column(db.Integer)

    price=db.Column(db.Float)
