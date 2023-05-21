'''below code is for Show table in database for my project showmaven, a ticket booking website for shows'''
from webapp import db
from datetime import datetime


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    rating = db.Column(db.Float)
    tags = db.Column(db.String(120))
    ticket_price = db.Column(db.Float)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Show {self.name}>'
    
    def __str__(self):
        return f'Show {self.name}'
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_rating(self):
        return self.rating
    
    def get_tags(self):
        return self.tags
    
    def get_ticket_price(self):
        return self.ticket_price
    
    def get_venue_id(self):
        return self.venue_id
    
    def get_created_at(self):
        return self.created_at
    
    def set_name(self, name):
        self.name = name

    def set_rating(self, rating):
        self.rating = rating

    def set_tags(self, tags):
        self.tags = tags








# from webapp import db


# class Show(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), index=True, unique=True)
#     rating = db.Column(db.Float)
#     tags = db.Column(db.String(120))
#     ticket_price = db.Column(db.Float)
#     venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))

#     def __repr__(self):
#         return f'<Show {self.name}>'


