'''below code is for user table in database for my project showmaven, a ticket booking website for shows'''
from webapp import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    '''below code is for user table in database for my project showmaven, a ticket booking website for shows'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def __str__(self):
        return f'User {self.username}'
    
    def get_id(self):
        return self.id
    
    def get_username(self):
        return self.username
    
    def get_created_at(self):
        return self.created_at
    
    def set_username(self, username):
        self.username = username
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def set_created_at(self, created_at):
        self.created_at = created_at





# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# from webapp import db, login_manager


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))

#     def __repr__(self):
#         return f'<User {self.username}>'

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))
