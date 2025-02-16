import sys
import os

# Add the project root (one level up) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from models import db
from factories.model_factory import create_owner, create_address, create_pet, create_tracker, create_activity_log

def seed_data():
    app = create_app()
    with app.app_context():
        # Reset the database
        db.drop_all()
        db.create_all()
        
        # Create sample data
        for _ in range(5):  # Create 5 owners
            owner = create_owner()
            create_address(owner.id)
            pet = create_pet(owner.id)
            create_tracker(pet.id)
            for _ in range(3):  # Create 3 activity logs per pet
                create_activity_log(pet.id)
        
        db.session.commit()
        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_data()
