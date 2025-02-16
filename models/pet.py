# models/pet.py
from extensions import db

class Pet(db.Model):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    tracker = db.relationship('Tracker', backref='pet', uselist=False)
    activity_logs = db.relationship('ActivityLog', backref='pet', lazy=True)
