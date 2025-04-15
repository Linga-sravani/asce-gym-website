from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    membership_plan = db.Column(db.String(50), nullable=False)

class MembershipPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255), default="https://via.placeholder.com/300x200?text=Service+Placeholder")

class Trainer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(200), nullable=False)
    expertise = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255), default="https://via.placeholder.com/300x300?text=Trainer+Placeholder")  # Default placeholder image

    # Add a relationship to ClassSchedule
    schedules = db.relationship('ClassSchedule', backref='trainer', lazy=True)

class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    session_name = db.Column(db.String(100), nullable=False)
    timing = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), default="https://via.placeholder.com/200x150?text=Class+Image")

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)