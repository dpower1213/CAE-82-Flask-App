# Intializing things
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_cors import CORS
import os
# init my Login Manager
login = LoginManager()
# Do inits for database stuff
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()

# NEW
if os.environ.get('FLASK_ENV') == 'development':
    cors= CORS()

def create_app(config_class=Config):
    #init the app
    app = Flask(__name__)

    #link our config to our app
    app.config.from_object(config_class)

    # register plugins
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    #NEW
    if os.environ.get('FLASK_ENV') == 'development':
        cors.init_app(app)

    # This is where you will be sent if you are not logged
    login.login_view='auth.login' 
    login.login_message = 'Log your punk *** into the website first'
    login.login_message_category='warning'

    moment.init_app(app)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.social import bp as social_bp
    app.register_blueprint(social_bp)

    from .blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    from .import exmodel, sql_demo_models
    
    return app

