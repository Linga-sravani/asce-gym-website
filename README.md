# ASCE Gym Website

A Flask-based web application for managing gym memberships, schedules, trainers, and more.

## Features
- **Homepage**: A dynamic landing page introducing ASCE Gym.
- **Membership Registration**: Users can sign up for memberships and view available plans.
- **Class Schedule**: Displays workout sessions, timings, and trainers.
- **Trainer Profiles**: Profiles of gym trainers with qualifications and expertise.
- **Pricing Structure**: Clear pricing for membership tiers and services.
- **Blog Section**: Fitness-related articles and updates.
- **Contact Page**: Contact details with an inquiry form.

## Technologies Used
- Flask (Python)
- Flask-SQLAlchemy (Database ORM)
- Flask-Login (User Authentication)
- Flask-Bcrypt (Password Hashing)
- MySQL (Database)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/username/asce-gym-website.git
2. Install dependencies:

pip install -r requirements.txt
Set up the MySQL database and update the SQLALCHEMY_DATABASE_URI in app.py.
Run the application:
python app.py
