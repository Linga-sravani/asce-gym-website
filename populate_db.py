from app import app
from database import db, MembershipPlan, Trainer, ClassSchedule, BlogPost

with app.app_context():
    db.drop_all()  # Clear existing data
    db.create_all()  # Recreate tables

    # Add membership plans
    db.session.add(MembershipPlan(name='Basic', price=50, description='Access to gym facilities'))
    db.session.add(MembershipPlan(name='Premium', price=100, description='Personal training included'))

    # Add trainers
    trainer1 = Trainer(name='John Doe', qualification='Certified Fitness Trainer', expertise='Strength Training')
    trainer2 = Trainer(name='Jane Smith', qualification='Yoga Instructor', expertise='Flexibility Training')
    db.session.add(trainer1)
    db.session.add(trainer2)

    # Add class schedules
    db.session.add(ClassSchedule(trainer_id=1, session_name='Strength Training', timing='6:00 AM - 7:00 AM'))
    db.session.add(ClassSchedule(trainer_id=2, session_name='Yoga', timing='8:00 AM - 9:00 AM'))

    # Add blog posts
    db.session.add(BlogPost(title='Benefits of Strength Training', content='Strength training improves muscle mass...'))
    db.session.add(BlogPost(title='Morning Yoga Routine', content='Start your day with these simple yoga poses...'))

    db.session.commit()