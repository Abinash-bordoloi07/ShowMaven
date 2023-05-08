from webapp import app, login_manager
from flask import render_template, request, session, redirect, flash, url_for
from flask_login import current_user
from webapp.models import Venue, Show, LoginForm, User, Ticket
from webapp import db


@app.route('/')
def home():
    return render_template('home.html', current_user=current_user)

@app.route('/search_venue', methods=['GET', 'POST'])
def search_venue():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        # Use the search_term to search for venues in the database
        venues = Venue.query.filter(or_(Venue.name.ilike(f'%{search_term}%'), Venue.place.ilike(f'%{search_term}%')))
        return render_template('search_venue.html', venues=venues, search_term=search_term)
    else:
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        # Check if the username and password are correct
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if username == 'admin' and password == 'passsword' and email == 'admin@mail.com':
            # Set the session variable for the admin user
            session['admin'] = True
            return redirect('/admin')
        else:
            # Set the session variable for the regular user
            session['admin'] = False
            session['username'] = username
            return redirect('/user')
    else:

        return render_template('login.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    """ Flask-Login user loader """

    return User.query.get(int(user_id))


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
        show = Show(name=name, rating=rating, tags=tags,
                    ticket_price=ticket_price, venue_id=venue_id)
        db.session.add(show)
        db.session.commit()
        flash('Show created successfully!', 'success')
        return redirect(url_for('shows'))
    return render_template('create_show.html', venues=venues)


@app.route('/admin/edit_show/int:show_id', methods=['GET', 'POST'])
def edit_show(show_id):
    show = Show.query.get_or_404(show_id)
    venues = Venue.query.all()
    if request.method == 'POST':
        show.name = request.form['name']
        show.rating = request.form['rating']
        show.tags = request.form['tags']
        show.ticket_price = request.form['ticket_price']
        show.venue_id = request.form['venue_id']
        db.session.commit()
        flash('Show updated successfully!', 'success')
        return redirect(url_for('shows'))
    return render_template('edit_show.html', show=show, venues=venues)


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
            flash('Sorry, only {} seats are available for this show.'.format(
                available_seats))
            return redirect(url_for('book_ticket', show_id=show_id))

        user_id = current_user.id
        for i in range(num_tickets):
            ticket = Ticket(user_id=user_id, show_id=show_id)
            db.session.add(ticket)
        db.session.commit()

        flash('Booking successful!')
        return redirect(url_for('user'))

    return render_template('book_ticket.html', show=show)
