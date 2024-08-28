from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy database instance
db = SQLAlchemy()

# Name of the database file
DB_NAME = "database.db"


def create_app():
    """Create and configure the Flask application."""
    # Create Flask app
    app = Flask(__name__)

    # Configure secret key for session management
    app.config['SECRET_KEY'] = 'ghghaasoi kdhjsdjn'

    # Set the URI for the SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Import views and authentication blueprints
    from .views import views
    from .auth import auth

    # Register blueprints for views and authentication
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import User and Note models
    from .models import User, Note

    # Create all database tables within the application context
    with app.app_context():
        db.create_all()

    # Initialize Flask-Login extension
    login_manager = LoginManager()

    # Set the login view for unauthorized users
    login_manager.login_view = 'auth.login'

    # Initialize Flask-Login with the Flask app
    login_manager.init_app(app)

    # User loader function to load user object based on user ID
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Return the Flask app
    return app


def create_database(app):
    """Create the database if it doesn't exist."""
    if not path.exists('website/' + DB_NAME):
        # Create all database tables if the database file doesn't exist
        db.create_all(app=app)
        print('Created Database!')
