"""Relational database for Uber Melon Tasting App in SQLAlchemy"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Creates a table to save user data."""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(99), unique=True)

    reservations = db.relationship("Reservation", back_populates="user")

     def __repr__(self):
        return f'<User object user_id: {self.user_id} email: {self.email}>'

class Reservation(db.Model):
    """Creates a table to save reservation data."""

    __tablename__ = 'reservations'
    res_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    res_dt = db.Column(db.DateTime, unique=True)

    user = db.relationship("User", back_populates="reservations")

# ============ DB/__name__ ============ #

def connect_to_db(flask_app, db_uri="postgresql:///melontastingDB", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
    db.create_all()