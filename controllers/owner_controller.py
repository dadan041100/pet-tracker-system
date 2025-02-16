# controllers/owner_controller.py
from flask import Blueprint, jsonify, request
from models.owner import Owner
from models import db

owner_bp = Blueprint('owner', __name__)

@owner_bp.route('/', methods=['GET'])
def get_owners():
    owners = Owner.query.all()
    data = [{
        'id': o.id,
        'name': o.name,
        'age': o.age,
        'email': o.email,
        'contact_number': o.contact_number,
        'backup_contact_number': o.backup_contact_number,
        'easy_contact_account': o.easy_contact_account
    } for o in owners]
    return jsonify(data)

@owner_bp.route('/', methods=['POST'])
def create_owner():
    data = request.get_json()
    owner = Owner(
        name=data['name'],
        age=data['age'],
        email=data['email'],
        contact_number=data['contact_number'],
        backup_contact_number=data['backup_contact_number'],
        easy_contact_account=data['easy_contact_account']
    )
    db.session.add(owner)
    db.session.commit()
    return jsonify({'message': 'Owner created successfully', 'owner_id': owner.id}), 201
