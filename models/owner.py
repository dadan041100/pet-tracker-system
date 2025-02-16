# models/owner.py
from extensions import db

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    backup_contact_number = db.Column(db.String(20), nullable=False)
    easy_contact_account = db.Column(db.String(255), nullable=False)
    
    addresses = db.relationship('Address', backref='owner', lazy=True)
    pets = db.relationship('Pet', backref='owner', lazy=True)
