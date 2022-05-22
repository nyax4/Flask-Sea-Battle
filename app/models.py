from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, login
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    wins_count = db.Column(db.Integer)
    lost_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def counts_plusplus(self, win_or_not):
        if self.wins_count == None:
            self.wins_count = 0
        if self.lost_count == None:
            self.lost_count = 0
        if win_or_not == 1:
            self.wins_count = self.wins_count + 1
        else:
            self.lost_count = self.lost_count + 1

