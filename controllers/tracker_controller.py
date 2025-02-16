# controllers/tracker_controller.py
from flask import Blueprint, jsonify, request
from models.tracker import Tracker
from models import db
from datetime import datetime

tracker_bp = Blueprint('tracker', __name__)

@tracker_bp.route('/', methods=['GET'])
def get_trackers():
    trackers = Tracker.query.all()
    data = []
    for t in trackers:
        # Access the related pet using the relationship defined in your models
        pet = t.pet  # Assuming you have defined: tracker = db.relationship('Tracker', backref='pet', uselist=False) in Pet
        data.append({
            'id': t.id,
            'pet_id': t.pet_id,
            'last_seen_location': t.last_seen_location,  # Should be "lat, lon"
            'last_seen_time': t.last_seen_time.isoformat(),
            'status': t.status,
            # Include pet details from your seeder
            'pet_name': pet.name if pet else 'Unknown',
            'pet_type': pet.type if pet else 'Unknown',
            'pet_breed': pet.breed if pet else 'Unknown',
            'pet_gender': pet.gender if pet else 'Unknown',
            'pet_age': pet.age if pet else 'Unknown',
            'pet_description': pet.description if pet else 'No description available'
        })
    return jsonify(data)

@tracker_bp.route('/', methods=['POST'])
def update_tracker():
    data = request.get_json()
    tracker = Tracker.query.filter_by(pet_id=data['pet_id']).first()
    if not tracker:
        tracker = Tracker(
            pet_id=data['pet_id'],
            last_seen_location=data['last_seen_location'],
            last_seen_time=datetime.strptime(data['last_seen_time'], '%Y-%m-%dT%H:%M:%S'),
            status=data['status']
        )
        db.session.add(tracker)
    else:
        tracker.last_seen_location = data['last_seen_location']
        tracker.last_seen_time = datetime.strptime(data['last_seen_time'], '%Y-%m-%dT%H:%M:%S')
        tracker.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Tracker updated successfully'}), 200
