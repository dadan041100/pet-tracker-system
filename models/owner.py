# models/owner.py
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    backup_contact_number = db.Column(db.String(20), nullable=False)
    easy_contact_account = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  # NEW field for password

    addresses = db.relationship('Address', backref='owner', lazy=True)
    pets = db.relationship('Pet', backref='owner', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
