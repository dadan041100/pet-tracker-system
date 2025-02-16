# Pet Tracker System

The **Pet Tracker System** is a full-stack project that integrates embedded hardware with a web application for real-time pet tracking. The system combines an Arduino Nano (with GSM and GPS modules) for capturing pet location data with a Flask web application that displays owner and pet information, tracking history, and an interactive map.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Hardware Components](#hardware-components)
- [Software Components](#software-components)
- [Installation](#installation)
- [Database Migrations & Seeding](#database-migrations--seeding)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

## Overview

The Pet Tracker System allows pet owners to monitor the location of their pets in real time via a web dashboard. Data is collected from hardware (Arduino with GSM & GPS) and stored in a database. The Flask application uses SQLAlchemy, Flask-Migrate, and Jinja2 for a complete full-stack solution with user authentication, dynamic data display, and interactive mapping using Leaflet.js.

## Features

- **Real-Time Pet Tracking:**  
  Displays pet location on an interactive map using Leaflet.js.

- **User Authentication:**  
  Basic login and logout functionality with session management, featuring modals to indicate logged in/out states.

- **Comprehensive Dashboard:**  
  Shows owner information, address details, pet profile (including image), and recent activity logs.

- **Database Migrations & Seeding:**  
  Uses Flask-Migrate and Faker to create and populate the database with sample data.

- **Modern, Responsive UI:**  
  A clean, professional design with a sidebar layout, modals, and responsive adjustments for various screen sizes.

## Hardware Components

- Arduino Nano  
- GSM Module  
- GPS Module  
- Battery, Voltage Regulator, Capacitors, Transistor  
- Jumper Wires, PCB, Breadboard

*The hardware captures real-time pet location and transmits the data to the web server.*

## Software Components

- Python 3.x  
- Flask (Web framework)  
- Flask-SQLAlchemy (ORM)  
- Flask-Migrate (Database migrations)  
- Jinja2 (Templating engine)  
- Leaflet.js (Interactive maps)  
- Faker (Database seeding)  

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/pet-tracker-system.git
   cd pet-tracker-system
   ```
2. **Create and Avtivate a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install the Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Environment Variables**
```bash
set FLASK_APP=app.py
set FLASK_ENV=development
```

## Database migration
1. **Initialize the migrations and migrate it
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
2. **Seed the Database**
```bash
python seeders/seed.py
```

## Start the Application 
``` bash
python app.py
```


