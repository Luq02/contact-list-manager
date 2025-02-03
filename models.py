from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Contact(db.Model):
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    type = db.Column(db.String(20), nullable=False)
    custom_type = db.Column(db.String(100), nullable=True)  # New field for custom type value
    is_favourite = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'type': self.type,
            'custom_type': self.custom_type,  # Include custom_type in the dictionary representation
            'is_favourite': self.is_favourite,
            'created_at': self.created_at.isoformat()
        }
