from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

# Define the routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            # Set the session variable for the admin user
            session['admin'] = True
            return redirect('/admin')
        else:
            # Set the session variable for the regular user
            session['admin'] = False
            session['username'] = username
            return redirect('/user')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the session variables
    session.clear()
    return redirect('/')

@app.route('/admin')
def admin():
    # Check if the user is an admin
    if not session.get('admin'):
        return redirect('/')
    return render_template('admin.html')

@app.route('/user')
def user():
    # Check if the user is a regular user
    if session.get('admin'):
        return redirect('/')
    username = session.get('username')
    return render_template('user.html', username=username)


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


@app.route('/book-ticket/<int:show_id>', methods=['GET', 'POST'])
def book_ticket(show_id):
    show = Show.query.get(show_id)
    if not show:
        flash('Show not found.')
        return redirect(url_for('home'))

    if request.method == 'POST':
        num_tickets = int(request.form['num_tickets'])
        if num_tickets <= 0:
            flash('Please select a valid number of tickets.')
            return redirect(url_for('book_ticket', show_id=show_id))

        available_seats = show.get_available_seats()
        if num_tickets > available_seats:
            flash('Sorry, only {} seats are available for this show.'.format(available_seats))
            return redirect(url_for('book_ticket', show_id=show_id))

        # user_id = current_user.id
        # for i in range(num_tickets):
        #     ticket = Ticket(user_id=user_id, show_id=show_id)
        #     db.session.add(ticket)
        # db.session.commit()

        flash('Booking successful!')
        return redirect(url_for('user'))

    return render_template('book_ticket.html', show=show)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search_results', methods=['POST'])
def search_results():
    location = request.form.get('location')
    tags = request.form.get('tags')
    rating = request.form.get('rating')
    shows = Show.query.filter_by(location=location, tags=tags, rating=rating).all()
    return render_template('search_results.html', shows=shows)


from app import db, Venue, Show

def update_ticket_prices():
    # Define your pricing model here
    # For example, you can increase the ticket prices by a certain percentage for popular shows
    # You can also decrease the ticket prices for less popular shows to encourage more bookings
    popular_shows = Show.query.filter_by(popularity=True).all()
    for show in popular_shows:
        show.ticket_price *= 1.2  # Increase the ticket price by 20%
        db.session.commit()
    less_popular_shows = Show.query.filter_by(popularity=False).all()
    for show in less_popular_shows:
        show.ticket_price *= 0.8  # Decrease the ticket price by 20%
        db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)
