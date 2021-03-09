from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from parrot.common import config

app = Flask(__name__)
app.config.from_object(config.environment)

__version__ = 0.1


DB_URL = 'postgresql+psycopg2://{user}:{password}@{host}/{db}'.format(user=app.config["POSTGRES_USER"],
                                                               password=app.config["POSTGRES_PASSWORD"],
                                                               host=app.config["POSTGRES_HOST"],
                                                               db=app.config["POSTGRES_DB"])

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


"""
importing models of the modules
"""

from parrot.orders.models import Orders
from parrot.users.models import Users


with app.app_context():
    db.init_app(app)
    db.create_all()


"""
Blueprints
"""

from parrot.orders.api import orders
from parrot.users.api import users
from parrot.reporting.api import reporting

app.register_blueprint(orders)
app.register_blueprint(users)
app.register_blueprint(reporting)
