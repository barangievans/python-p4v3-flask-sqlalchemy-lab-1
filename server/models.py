# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
