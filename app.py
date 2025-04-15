from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MySQL Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://if0_37434293:mIXHXlvrDfHaju@sql102.infinityfree.com/if0_37434293_gym'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    membership_plan = db.Column(db.String(50), nullable=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_name = db.Column(db.String(100), nullable=False)
    timing = db.Column(db.String(50), nullable=False)

# Load User for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', bookings=bookings)

@app.route('/membership', methods=['GET', 'POST'])
@login_required
def membership():
    if request.method == 'POST':
        plan = request.form['plan']
        current_user.membership_plan = plan
        db.session.commit()
        flash('Membership updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('membership.html')

@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    if request.method == 'POST':
        session_name = request.form['session_name']
        timing = request.form['timing']
        new_booking = Booking(user_id=current_user.id, session_name=session_name, timing=timing)
        db.session.add(new_booking)
        db.session.commit()
        flash('Booking successful!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('book.html')

@app.route('/schedule')
def schedule():
    schedule = [
        {'session_name': 'Strength Training', 'timing': '6:00 AM - 7:00 AM', 'trainer': 'John Doe'},
        {'session_name': 'Yoga', 'timing': '8:00 AM - 9:00 AM', 'trainer': 'Jane Smith'},
        {'session_name': 'Cardio', 'timing': '5:00 PM - 6:00 PM', 'trainer': 'Alice Johnson'},
    ]
    return render_template('schedule.html', schedule=schedule)

@app.route('/trainers')
def trainers():
    trainers = [
        {'name': 'John Doe', 'qualification': 'Certified Fitness Trainer', 'expertise': 'Strength Training'},
        {'name': 'Jane Smith', 'qualification': 'Yoga Instructor', 'expertise': 'Flexibility Training'},
        {'name': 'Alice Johnson', 'qualification': 'Nutritionist', 'expertise': 'Weight Management'},
    ]
    return render_template('trainers.html', trainers=trainers)

@app.route('/pricing')
def pricing():
    plans = [
        {'name': 'Basic Plan', 'price': '$50/month', 'features': ['Access to gym facilities', 'Group fitness classes']},
        {'name': 'Premium Plan', 'price': '$100/month', 'features': ['Personal training sessions', 'Nutrition consultation']},
    ]
    return render_template('pricing.html', plans=plans)

@app.route('/blog')
def blog():
    posts = [
        {'title': 'Benefits of Strength Training', 'content': 'Strength training helps build muscle, improve endurance, and boost metabolism.'},
        {'title': 'Healthy Eating Habits', 'content': 'Learn how to maintain a balanced diet for optimal fitness results.'},
    ]
    return render_template('blog.html', posts=posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Thank you for contacting us!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)