# ui_dashboard/auth/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """Set password (hash it using Werkzeug)"""
        self.password = password

    def check_password(self, password):
        """Check hashed password"""
        return self.password == password
