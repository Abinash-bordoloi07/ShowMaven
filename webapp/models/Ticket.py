'''below code is for ticket table in database for my project showmaven, a ticket booking website for shows'''

from webapp import db
from datetime import datetime



class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Ticket {self.id}>'
    
    def __str__(self):
        return f'Ticket {self.id}'
    
    def get_id(self):
        return self.id
    
    def get_show_id(self):
        return self.show_id
    
    def get_user_id(self):
        return self.user_id
    
    def get_price(self):
        return self.price
    
    def get_created_at(self):
        return self.created_at
    
    def set_show_id(self, show_id):
        self.show_id = show_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_price(self, price):
        self.price = price









# from datetime import datetime
# from webapp import db


# class Ticket(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     def __repr__(self):
#         return f'<Ticket {self.id}>'
    
#     def __str__(self):
#         return f'Ticket {self.id}'
    
#     def get_id(self):
#         return self.id
    
