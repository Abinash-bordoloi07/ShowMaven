from webapp import db


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(240))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    shows = db.relationship('Show', backref='venue', lazy='dynamic')

    def __repr__(self):
        return f'<Venue {self.name}>'
