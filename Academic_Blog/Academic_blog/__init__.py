from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# instantiate flask application meaning you can run it has the main file
app = Flask(__name__)

app.config['SECRET_KEY'] = '1f93e7e6d36df668b37999100b05ebb0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.databasedb'

#create a database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from Academic_blog import routes