# factories/model_factory.py
import random
from faker import Faker
from models import db
from models.owner import Owner
from models.address import Address
from models.pet import Pet
from models.tracker import Tracker
from models.activity_log import ActivityLog
from datetime import datetime, timedelta

fake = Faker()

def create_owner():
    # If no owners exist, use a known email; otherwise, use a random one.
    if Owner.query.count() == 0:
        email = "test@example.com"
    else:
        email = fake.unique.email()
    
    owner = Owner(
        name=fake.name(),
        age=random.randint(25, 60),
        email=email,
        contact_number=fake.phone_number(),
        backup_contact_number=fake.phone_number(),
        easy_contact_account=fake.user_name()
    )
    owner.set_password("test")  # Set the default password
    from extensions import db  # Ensure db is imported here if not already
    db.session.add(owner)
    db.session.flush()  # Flush to assign an id
    print(f"Created owner with email: {owner.email}")  # For debugging
    return owner



def create_address(owner_id):
    address = Address(
        owner_id=owner_id,
        city=fake.city(),
        municipality=fake.city(),
        village=fake.city_suffix(),
        barangay=fake.word(),
        street=fake.street_name(),
        blk_and_lot=f"{random.randint(1,100)}-{random.randint(1,50)}"
    )
    db.session.add(address)
    return address

def create_pet(owner_id):
    pet = Pet(
        owner_id=owner_id,
        name=fake.first_name(),
        type=random.choice(['Dog', 'Golden Retriever', 'Aspin']),
        breed=fake.word(),
        gender=random.choice(['Male', 'Female']),
        age=random.randint(1, 15),
        description=fake.text(max_nb_chars=200),
        image_url="/static/images/sample-dog.jpg"
    )
    db.session.add(pet)
    db.session.flush()  # Get pet.id
    return pet

def create_tracker(pet_id):
    base_lat = 14.5995
    base_lon = 120.9842
    # Add a small random offset (about ±0.02 degrees) for variation
    lat = base_lat + random.uniform(-0.02, 0.02)
    lon = base_lon + random.uniform(-0.02, 0.02)
    tracker = Tracker(
        pet_id=pet_id,
        last_seen_location=f"{lat:.4f}, {lon:.4f}",
        last_seen_time=datetime.utcnow() - timedelta(hours=random.randint(0, 24)),
        status=random.choice(['Active', 'Inactive', 'Lost'])
    )
    db.session.add(tracker)
    return tracker

def create_activity_log(pet_id):
    log = ActivityLog(
        pet_id=pet_id,
        activity_type=random.choice(['Move', 'Rest', 'Play']),
        description=fake.text(max_nb_chars=100),
        timestamp=datetime.utcnow() - timedelta(minutes=random.randint(0, 60))
    )
    db.session.add(log)
    return log
