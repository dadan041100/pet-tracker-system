# models/address.py
from extensions import db

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    municipality = db.Column(db.String(255), nullable=False)
    village = db.Column(db.String(255), nullable=True)
    barangay = db.Column(db.String(255), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    blk_and_lot = db.Column(db.String(255), nullable=False)
