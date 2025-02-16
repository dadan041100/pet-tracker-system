from flask import Flask, render_template, request, redirect, url_for, flash, session
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
    app.secret_key = 'supersecretkey'  # For session management
    
    # Initialize SQLAlchemy and Flask-Migrate
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register Blueprints
    app.register_blueprint(owner_bp, url_prefix='/owners')
    app.register_blueprint(pet_bp, url_prefix='/pets')
    app.register_blueprint(tracker_bp, url_prefix='/trackers')
    
    # --- Authentication Routes ---
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            owner = Owner.query.filter_by(email=email).first()
            if owner and owner.check_password(password):
                session['user'] = owner.email
                session.pop('logged_out', None)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid email or password', 'error')
                return render_template('login.html')
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.pop('user', None)
        session['logged_out'] = True
        flash('Logged out successfully!', 'success')
        return redirect(url_for('login'))
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            flash("Registration functionality is not implemented yet.", "info")
            return redirect(url_for('login'))
        return render_template('register.html')
    
    # --- Protected Routes ---
    @app.route('/', endpoint='home')
    def index():
        if 'user' not in session:
            return redirect(url_for('login'))
        current_owner = Owner.query.first()
        current_address = Address.query.filter_by(owner_id=current_owner.id).first() if current_owner else None
        current_pet = Pet.query.filter_by(owner_id=current_owner.id).first() if current_owner else None
        recent_activities = []
        if current_pet:
            recent_activities = (ActivityLog.query.filter_by(pet_id=current_pet.id)
                                 .order_by(ActivityLog.timestamp.desc())
                                 .limit(5)
                                 .all())
        return render_template(
            'index.html', 
            current_owner=current_owner,
            current_address=current_address,
            current_pet=current_pet,
            recent_activities=recent_activities
        )
    
    @app.route('/dashboard', endpoint='dashboard')
    def dashboard():
        if 'user' not in session:
            return redirect(url_for('login'))
        current_owner = Owner.query.first()
        current_pet = Pet.query.filter_by(owner_id=current_owner.id).first() if current_owner else None
        tracker = current_pet.tracker if current_pet else None
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
