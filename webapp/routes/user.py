'''create the user routes here defining all the routes for the user blueprint'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from webapp import db
from webapp.models.Show import Show
from webapp.models.Ticket import Ticket
from webapp.models.User import User
from webapp.forms import ShowForm, TicketForm, UserForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from webapp import login_manager

user_bp = Blueprint('user_bp', __name__, url_prefix='/user')

@user_bp.route('/')
@login_required
def index():
    '''this function is for the user index page in my project showmaven, a ticket booking website for shows'''
    return render_template('user/index.html')

@user_bp.route('/shows')
@login_required
def shows():
    '''this function is for the user shows page in my project showmaven, a ticket booking website for shows'''
    shows = Show.query.all()
    return render_template('user/shows.html', shows=shows)

@user_bp.route('/shows/<int:id>/book', methods=['GET', 'POST'])
@login_required
def book_show(id):
    '''this function is for the user book show page in my project showmaven, a ticket booking website for shows'''
    show = Show.query.get_or_404(id)
    form = TicketForm()
    if form.validate_on_submit():
        ticket = Ticket()
        form.populate_obj(ticket)
        ticket.show_id = show.id
        ticket.user_id = current_user.id
        db.session.add(ticket)
        db.session.commit()
        flash('Ticket booked successfully', 'success')
        return redirect(url_for('user.shows'))
    return render_template('user/book_show.html', form=form, show=show)

@user_bp.route('/tickets')
@login_required
def tickets():
    '''this function is for the user tickets page in my project showmaven, a ticket booking website for shows'''
    tickets = Ticket.query.filter_by(user_id=current_user.id).all()
    return render_template('user/tickets.html', tickets=tickets)

@user_bp.route('/tickets/<int:id>/cancel', methods=['GET', 'POST'])
@login_required
def cancel_ticket(id):
    '''this function is for the user cancel ticket page in my project showmaven, a ticket booking website for shows'''
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    flash('Ticket cancelled successfully', 'success')
    return redirect(url_for('user.tickets'))

