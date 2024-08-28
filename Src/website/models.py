from . import db  # Import the database instance created in __init__.py
from flask_login import UserMixin  # Import UserMixin for user authentication
from sqlalchemy.sql import func  # Import func for using database functions


# Define the Note class as a model for the 'note' table in the database
class Note(db.Model):
    """Model class for notes."""
    # Define 'id' as the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Define 'data' as a string column with a length of 10000 characters
    data = db.Column(db.String(10000))
    # Define 'date' as a datetime column with timezone, default value is current timestamp
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Define 'user_id' as a foreign key referencing the 'id' column in the 'user' table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# Define the User class as a model for the 'user' table in the database, inheriting from UserMixin for user authentication
class User(db.Model, UserMixin):
    """Model class for users."""
    # Define 'id' as the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Define 'email' as a unique string column with a length of 150 characters
    email = db.Column(db.String(150), unique=True)
    # Define 'password' as a string column with a length of 150 characters
    password = db.Column(db.String(150))
    # Define 'first_name' as a string column with a length of 150 characters
    first_name = db.Column(db.String(150))
    # Define a one-to-many relationship with the 'Note' model
    notes = db.relationship('Note')
