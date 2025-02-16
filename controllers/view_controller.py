from flask import Blueprint, render_template
from services.database import Database
from models import Pet, Tracker

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def dashboard():
    session = Database.get_session()
    pets = session.query(Pet).join(Tracker).all()
    return render_template('dashboard.html', pets=pets)

@views_bp.route('/map')
def map_view():
    return render_template('map.html')

@views_bp.route('/activity/<int:pet_id>')
def activity_logs(pet_id):
    session = Database.get_session()
    pet = session.query(Pet).get(pet_id)
    return render_template('activity_logs.html', pet=pet)