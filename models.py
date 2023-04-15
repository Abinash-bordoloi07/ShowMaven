from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_manager, current_app
from datetime import datetime
db = SQLAlchemy()
from . import api

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    with current_app.app_context():
        return User.query.get(int(user_id))


class Engagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    event_name = db.Column(db.String(100))
    event_date = db.Column(db.DateTime)


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)

class VenueShow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    venue = db.relationship('Venue', backref=db.backref('venue_shows', lazy=True))
    show = db.relationship('Show', backref=db.backref('venue_shows', lazy=True))

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    venue_show_id = db.Column(db.Integer, db.ForeignKey('venue_show.id'), nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False)
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    venue_show = db.relationship('VenueShow', backref=db.backref('bookings', lazy=True))

