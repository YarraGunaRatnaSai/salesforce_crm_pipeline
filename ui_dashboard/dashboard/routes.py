from flask import Blueprint, render_template
from ui_dashboard.auth.routes import auth_bp

# Blueprint for dashboard routes
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Home route
@dashboard_bp.route('/')
def home():
    """
    Route to display the dashboard home page.
    """
    return render_template('user_dashboard.html')

# Add additional dashboard-related routes here
@dashboard_bp.route('/profile')
def profile():
    """
    Route to display the user profile.
    """
    return render_template('user_profile.html')

# Register authentication blueprint
def init_app(app):
    """
    Initialize the routes for the dashboard.
    """
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
