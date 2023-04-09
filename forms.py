from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


class VenueForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120)])
    location = StringField('Location', validators=[DataRequired(), Length(max=120)])
    description = TextAreaField('Description', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired()])


class ShowForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=120)])
    artist = StringField('Artist', validators=[DataRequired(), Length(max=120)])
    venue_id = SelectField('Venue', coerce=int)
    start_time = DateField('Start Time', validators=[DataRequired()])
