from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'feb18e2b6945bba740f71cf219b4b49b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# when ran directly i.e.python run.py, the __name__ variable is '__main__'
# ran from another module i.e. python -m flask run, the __name__ variable is the filename i.e.'flaskblog'

from flaskblog import routes
