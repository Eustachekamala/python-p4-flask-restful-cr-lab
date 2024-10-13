from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy_serializer import SerializerMixin # type: ignore

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String(200))
    price = db.Column(db.Float)
