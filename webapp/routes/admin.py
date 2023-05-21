'''create the admin routes code here defining all the routes for the admin in my project showmaven, a ticket booking website for shows'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from webapp import db
from webapp.exception_handle import exception_handler
from webapp.models.Show import Show
from webapp.models.Booking import Booking
from webapp.models.Venue import Venue
from webapp.models.Ticket import Ticket
from webapp.models.User import User
from webapp.forms import ShowForm, TicketForm, UserForm, BookingForm,VenueForm
from webapp.forms import ShowForm, TicketForm, UserForm
from werkzeug.security import generate_password_hash, check_password_hash




admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/')
@login_required
@exception_handler
def index():
    '''this function is for the admin index page in my project showmaven, a ticket booking website for shows'''
    return render_template('admin/index.html')
'''route for admin dashboard'''
@admin_bp.route('/dashboard')
@login_required
@exception_handler
def dashboard():
    '''this function is for the admin dashboard page in my project showmaven, a ticket booking website for shows'''
    return render_template('admin/dashboard.html')




@admin_bp.route('/shows')
@login_required
@exception_handler
def shows():
    '''this function is for the admin shows page in my project showmaven, a ticket booking website for shows'''
    shows = Show.query.all()
    return render_template('admin/shows.html', shows=shows)

@admin_bp.route('/shows/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_show():
    '''this function is for the admin create show page in my project showmaven, a ticket booking website for shows'''
    form = ShowForm()
    if form.validate_on_submit():
        show = Show()
        form.populate_obj(show)
        db.session.add(show)
        db.session.commit()
        flash('Show created successfully', 'success')
        return redirect(url_for('admin.shows'))
    return render_template('admin/create_show.html', form=form)

@admin_bp.route('/shows/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_show(id):
    '''this function is for the admin edit show page in my project showmaven, a ticket booking website for shows'''
    show = Show.query.get_or_404(id)
    form = ShowForm(obj=show)
    if form.validate_on_submit():
        form.populate_obj(show)
        db.session.commit()
        flash('Show updated successfully', 'success')
        return redirect(url_for('admin.shows'))
    return render_template('admin/edit_show.html', form=form)


@admin_bp.route('/shows/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler 
def delete_show(id):
    '''this function is for the admin delete show page in my project showmaven, a ticket booking website for shows'''
    show = Show.query.get_or_404(id)
    db.session.delete(show)
    db.session.commit()
    flash('Show deleted successfully', 'success')
    return redirect(url_for('admin.shows'))

@admin_bp.route('/tickets')
@login_required
@exception_handler
def tickets():
    '''this function is for the admin tickets page in my project showmaven, a ticket booking website for shows'''
    tickets = Ticket.query.all()
    return render_template('admin/tickets.html', tickets=tickets)

@admin_bp.route('/tickets/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_ticket():
    '''this function is for the admin create ticket page in my project showmaven, a ticket booking website for shows'''
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket()
        form.populate_obj(ticket)
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket created successfully', 'success')
        return redirect(url_for('admin.tickets'))
    return render_template('admin/create_ticket.html', form=form)

@admin_bp.route('/tickets/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_ticket(id):
    '''edit ticket'''
    ticket = Ticket.query.get_or_404(id)
    form = TicketForm(obj=ticket)
    if form.validate_on_submit():
        form.populate_obj(ticket)
        db.session.commit()
        flash('Ticket updated successfully', 'success')
        return redirect(url_for('admin.tickets'))
    return render_template('admin/edit_ticket.html', form=form)

@admin_bp.route('/tickets/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler
def delete_ticket(id):
    '''delete ticket'''
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket deleted successfully', 'success')
    return redirect(url_for('admin.tickets'))

@admin_bp.route('/users')
@login_required
@exception_handler
def users():
    '''this function is for the admin users page in my project showmaven, a ticket booking website for shows'''
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_user():
    '''this function is for the admin create user page in my project showmaven, a ticket booking website for shows'''
    form = UserForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/create_user.html', form=form)



@admin_bp.route('/users/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_user(id):
    '''edit user'''
    user = User.query.get_or_404(id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        '''form.populate_obj(user)'''
        user.username = form.username.data
        user.email = form.email.data
        user.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash('User updated successfully', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/edit_user.html', form=form)

@admin_bp.route('/users/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler
def delete_user(id):
    '''delete user'''
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully', 'success')
    return redirect(url_for('admin.users'))

@admin_bp.route('/bookings')
@login_required
@exception_handler
def bookings():
    '''this function is for the admin bookings page in my project showmaven, a ticket booking website for shows'''
    bookings = Booking.query.all()
    return render_template('admin/bookings.html', bookings=bookings)

@admin_bp.route('/bookings/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_booking():
    '''this function is for the admin create booking page in my project showmaven, a ticket booking website for shows'''
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking()
        form.populate_obj(booking)
        db.session.add(booking)
        db.session.commit()
        flash('Booking created successfully', 'success')
        return redirect(url_for('admin.bookings'))
    return render_template('admin/create_booking.html', form=form)

@admin_bp.route('/bookings/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_booking(id):
    '''edit booking'''
    booking = Booking.query.get_or_404(id)
    form = BookingForm(obj=booking)
    if form.validate_on_submit():
        form.populate_obj(booking)
        db.session.commit()
        flash('Booking updated successfully', 'success')
        return redirect(url_for('admin.bookings'))
    return render_template('admin/edit_booking.html', form=form)

@admin_bp.route('/bookings/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler
def delete_booking(id):
    '''delete booking'''
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    flash('Booking deleted successfully', 'success')
    return redirect(url_for('admin.bookings'))

@admin_bp.route('/shows')
@login_required
@exception_handler
def shows():
    '''this function is for the admin shows page in my project showmaven, a ticket booking website for shows'''
    shows = Show.query.all()
    return render_template('admin/shows.html', shows=shows)

@admin_bp.route('/shows/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_show():
    '''this function is for the admin create show page in my project showmaven, a ticket booking website for shows'''
    form = ShowForm()
    if form.validate_on_submit():
        show = Show()
        form.populate_obj(show)
        db.session.add(show)
        db.session.commit()
        flash('Show created successfully', 'success')
        return redirect(url_for('admin.shows'))
    return render_template('admin/create_show.html', form=form)

@admin_bp.route('/shows/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_show(id):
    '''edit show'''
    show = Show.query.get_or_404(id)
    form = ShowForm(obj=show)
    if form.validate_on_submit():
        form.populate_obj(show)
        db.session.commit()
        flash('Show updated successfully', 'success')
        return redirect(url_for('admin.shows'))
    return render_template('admin/edit_show.html', form=form)

@admin_bp.route('/shows/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler
def delete_show(id):
    '''delete show'''
    show = Show.query.get_or_404(id)
    db.session.delete(show)
    db.session.commit()
    flash('Show deleted successfully', 'success')
    return redirect(url_for('admin.shows'))

@admin_bp.route('/venues')
@login_required
@exception_handler
def venues():
    '''this function is for the admin venues page in my project showmaven, a ticket booking website for shows'''
    venues = Venue.query.all()
    return render_template('admin/venues.html', venues=venues)


'''give me the edit_show.html template code'''

@admin_bp.route('/venues/create', methods=['GET', 'POST'])
@login_required
@exception_handler
def create_venue():
    '''this function is for the admin create venue page in my project showmaven, a ticket booking website for shows'''
    form = VenueForm()
    if form.validate_on_submit():
        venue = Venue()
        form.populate_obj(venue)
        db.session.add(venue)
        db.session.commit()
        flash('Venue created successfully', 'success')
        return redirect(url_for('admin.venues'))
    return render_template('admin/create_venue.html', form=form)

@admin_bp.route('/venues/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@exception_handler
def edit_venue(id):
    'edit venue'
    venue = Venue.query.get_or_404(id)
    form = VenueForm(obj=venue)
    if form.validate_on_submit():
        form.populate_obj(venue)
        db.session.commit()
        flash('Venue updated successfully', 'success')
        return redirect(url_for('admin.venues'))
    return render_template('admin/edit_venue.html', form=form)

@admin_bp.route('/venues/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@exception_handler
def delete_venue(id):
    '''delete venue'''
    venue = Venue.query.get_or_404(id)
    db.session.delete(venue)
    db.session.commit()
    flash('Venue deleted successfully', 'success')
    return redirect(url_for('admin.venues'))
