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
    owner = Owner(
        name=fake.name(),
        age=random.randint(25, 60),
        email=fake.unique.email(),
        contact_number=fake.phone_number(),
        backup_contact_number=fake.phone_number(),
        easy_contact_account=fake.user_name()
    )
    db.session.add(owner)
    db.session.flush()  # Get owner.id without committing
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
        type=random.choice(['Dog', 'Cat', 'Bird']),
        breed=fake.word(),
        gender=random.choice(['Male', 'Female']),
        age=random.randint(1, 15),
        description=fake.text(max_nb_chars=200)
    )
    db.session.add(pet)
    db.session.flush()  # Get pet.id
    return pet

def create_tracker(pet_id):
    # Hardcoding a sample coordinate around Metro Manila for testing
    tracker = Tracker(
        pet_id=pet_id,
        last_seen_location="14.5995, 120.9842",  # Metro Manila coordinates
        last_seen_time=datetime.utcnow() - timedelta(hours=random.randint(0, 24)),
        status=random.choice(['Active', 'Inactive', 'Lost'])
    )
    db.session.add(tracker)
    return tracker

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
