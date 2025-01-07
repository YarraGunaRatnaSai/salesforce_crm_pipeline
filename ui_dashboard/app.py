from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from ui_dashboard.auth.routes import auth_bp
from ui_dashboard.auth.models import db
from ui_dashboard.dashboard.routes import dashboard_bp
from ui_dashboard.dashboard.routes import init_app as init_dashboard_routes
from config import load_config

# Initialize Flask application
app = Flask(__name__)

# Load the configuration based on the environment (e.g., "development" or "production")
config = load_config("development")  # Change to "production" for production settings

# Set up Flask app with loaded configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@localhost/{config['DB_NAME']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = config['SECRET_KEY']  # Use SECRET_KEY from the YAML file

# Initialize the dashboard routes
init_dashboard_routes(app)

# Initialize db and register blueprints
db = SQLAlchemy(app)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
