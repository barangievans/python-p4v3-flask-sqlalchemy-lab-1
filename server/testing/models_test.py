# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    # Define the columns for the Earthquake table
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    # Optional: Custom serialization
    def to_dict(self):
        return {
            'id': self.id,
            'magnitude': self.magnitude,
            'location': self.location,
            'year': self.year
        }
