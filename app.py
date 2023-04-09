from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ticket_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'
db = SQLAlchemy(app)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    place = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    shows = db.relationship('Show', backref='venue', lazy=True)

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)

@app.route('/admin/venues')
def venues():
    venues = Venue.query.all()
    return render_template('venues.html', venues=venues)

@app.route('/admin/create_venue', methods=['GET', 'POST'])
def create_venue():
    if request.method == 'POST':
        name = request.form['name']
        place = request.form['place']
        capacity = request.form['capacity']
        venue = Venue(name=name, place=place, capacity=capacity)
        db.session.add(venue)
        db.session.commit()
        flash('Venue created successfully!', 'success')
        return redirect(url_for('venues'))
    return render_template('create_venue.html')

@app.route('/admin/edit_venue/<int:id>', methods=['GET', 'POST'])
def edit_venue(id):
    venue = Venue.query.get_or_404(id)
    if request.method == 'POST':
        venue.name = request.form['name']
        venue.place = request.form['place']
        venue.capacity = request.form['capacity']
        db.session.commit()
        flash('Venue updated successfully!', 'success')
        return redirect(url_for('venues'))
    return render_template('edit_venue.html', venue=venue)

@app.route('/admin/delete_venue/<int:id>', methods=['POST'])
def delete_venue(id):
    venue = Venue.query.get_or_404(id)
    db.session.delete(venue)
    db.session.commit()
    flash('Venue deleted successfully!', 'success')
    return redirect(url_for('venues'))

@app.route('/admin/shows')
def shows():
    shows = Show.query.all()
    return render_template('shows.html', shows=shows)

@app.route('/admin/create_show', methods=['GET', 'POST'])
def create_show():
    venues = Venue.query.all()
    if request.method == 'POST':
        name = request.form['name']
        rating = request.form['rating']
        tags = request.form['tags']
        ticket_price = request.form['ticket_price']
        venue_id = request.form['venue_id']
        show = Show(name=name, rating=rating, tags=tags, ticket_price=ticket_price, venue_id=venue_id)
        db.session.add(show)
        db.session.commit()
        flash('Show created successfully!', 'success')
        return redirect(url_for('shows'))
    return render_template('create_show.html', venues=venues)

# @app.route('/admin/edit_show/<int:id>', methods=['GET', 'POST'])
# def edit_show(id):
#     show = Show.query.get_or_404(id)
#     venues = Venue.query.all()
#     if
