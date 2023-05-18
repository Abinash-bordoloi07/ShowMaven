from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # Register blueprints for routes
    from .routes.admin import admin_bp
    from .routes.user import user_bp
    from .routes.home import home_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(home_bp)


    # Import models to create database tables
    from .models import user, venue, show, ticket

    return app