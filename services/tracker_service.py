# services/tracker_service.py
from models.tracker import Tracker
from models import db
from datetime import datetime

def update_tracker_location(pet_id, location, status):
    tracker = Tracker.query.filter_by(pet_id=pet_id).first()
    if tracker:
        tracker.last_seen_location = location
        tracker.last_seen_time = datetime.utcnow()
        tracker.status = status
    else:
        tracker = Tracker(
            pet_id=pet_id,
            last_seen_location=location,
            last_seen_time=datetime.utcnow(),
            status=status
        )
        db.session.add(tracker)
    db.session.commit()
    return tracker
