#!/usr/bin/env python3
# server/seed.py

# seed.py
from models import db, Pet
from faker import Faker

fake = Faker()

def seed_pets(num_pets=10):
    for _ in range(num_pets):
        pet = Pet(
            name=fake.first_name(),
            species=fake.random_element(elements=('Dog', 'Cat', 'Hamster', 'Turtle', 'Chicken'))
        )
        db.session.add(pet)
    db.session.commit()

if __name__ == '__main__':
    from app import app
    with app.app_context():
        db.create_all()  # Ensure tables are created
        seed_pets()  # Call the seeding function

