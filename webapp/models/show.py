from webapp import db


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Float)
    tags = db.Column(db.String(120))
    ticket_price = db.Column(db.Float)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

    def __repr__(self):
        return f'<Show {self.name}>'

