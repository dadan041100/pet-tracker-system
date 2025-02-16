from flask import Flask, render_template
from config import Config
from extensions import db
from flask_migrate import Migrate
from models.owner import Owner
from models.address import Address
from models.pet import Pet
from models.activity_log import ActivityLog
from controllers.owner_controller import owner_bp
from controllers.pet_controller import pet_bp
from controllers.tracker_controller import tracker_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register Blueprints
    app.register_blueprint(owner_bp, url_prefix='/owners')
    app.register_blueprint(pet_bp, url_prefix='/pets')
    app.register_blueprint(tracker_bp, url_prefix='/trackers')
    
    # Main routes
    @app.route('/', endpoint='home')
    def index():
        # For simplicity, grab the first owner from the database
        current_owner = Owner.query.first()
        # Retrieve the owner's address, pet, and recent activity (adjust your query as needed)
        current_address = Address.query.filter_by(owner_id=current_owner.id).first()
        current_pet = Pet.query.filter_by(owner_id=current_owner.id).first()
        recent_activities = ActivityLog.query.filter_by(pet_id=current_pet.id)\
                                            .order_by(ActivityLog.timestamp.desc())\
                                            .limit(5).all()
        return render_template(
            'index.html', 
            current_owner=current_owner,
            current_address=current_address,
            current_pet=current_pet,
            recent_activities=recent_activities
        )
    
    @app.route('/dashboard', endpoint='dashboard')
    def dashboard():
        # Again, retrieve current owner/pet data
        current_owner = Owner.query.first()
        current_pet = Pet.query.filter_by(owner_id=current_owner.id).first()
        # Optionally, you might also query tracker data here if needed
        tracker = current_pet.tracker  # Assuming a one-to-one relationship
        return render_template(
            'dashboard.html', 
            current_owner=current_owner,
            current_pet=current_pet,
            tracker=tracker
        )
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5001)
