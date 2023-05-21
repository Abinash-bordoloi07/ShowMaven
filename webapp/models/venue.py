'''below code is for venue table in database for my project showmaven, a ticket booking website for shows'''
from webapp import db
from datetime import datetime


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(240))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    country = db.Column(db.String(120))
    phone = db.Column(db.String(30))
    shows = db.relationship('Show', backref='venue', lazy='dynamic')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Venue {self.name}>'
    
    def __str__(self):
        return f'Venue {self.name}'
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state
    
    def get_country(self):
        return self.country
    
    def get_phone(self):
        return self.phone
    
    def get_created_at(self):
        return self.created_at
    
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_country(self, country):
        self.country = country

    def set_phone(self, phone):
        self.phone = phone


        




# from webapp import db


# class Venue(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), index=True, unique=True)
#     address = db.Column(db.String(240))
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     country = db.Column(db.String(120))
#     phone = db.Column(db.String(30))
#     shows = db.relationship('Show', backref='venue', lazy='dynamic')

#     def __repr__(self):
#         return f'<Venue {self.name}>'
