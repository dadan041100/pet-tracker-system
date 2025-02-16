# controllers/pet_controller.py
from flask import Blueprint, jsonify, request
from models.pet import Pet
from models import db

pet_bp = Blueprint('pet', __name__)

@pet_bp.route('/', methods=['GET'])
def get_pets():
    pets = Pet.query.all()
    data = [{
        'id': p.id,
        'owner_id': p.owner_id,
        'name': p.name,
        'type': p.type,
        'breed': p.breed,
        'gender': p.gender,
        'age': p.age,
        'description': p.description
    } for p in pets]
    return jsonify(data)

@pet_bp.route('/', methods=['POST'])
def create_pet():
    data = request.get_json()
    pet = Pet(
        owner_id=data['owner_id'],
        name=data['name'],
        type=data['type'],
        breed=data['breed'],
        gender=data['gender'],
        age=data['age'],
        description=data.get('description', '')
    )
    db.session.add(pet)
    db.session.commit()
    return jsonify({'message': 'Pet created successfully', 'pet_id': pet.id}), 201
