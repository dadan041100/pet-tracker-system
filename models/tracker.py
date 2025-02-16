# models/tracker.py
from extensions import db

class Tracker(db.Model):
    __tablename__ = 'tracker'
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
    last_seen_location = db.Column(db.String(255), nullable=False)
    last_seen_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
