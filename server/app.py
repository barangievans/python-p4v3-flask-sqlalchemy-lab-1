from flask import Flask, jsonify, current_app
from flask_sqlalchemy import SQLAlchemy
from models import db, Earthquake

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Initialize the database
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Route to get an earthquake by ID
@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    with current_app.app_context():
        earthquake = db.session.get(Earthquake, id)
    if earthquake:
        return jsonify(earthquake.serialize()), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

# Route to get earthquakes by minimum magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(quakes),
        "quakes": [quake.serialize() for quake in quakes]
    }), 200

# Run the application
if __name__ == '__main__':
    app.run(port=5555)
