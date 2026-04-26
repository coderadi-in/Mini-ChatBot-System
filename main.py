# ==================================================
# ! LOAD VENV
# ==================================================

from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ==================================================
# ? IMPORTS
# ==================================================

from flask import Flask, redirect, url_for
import os
from models.user import User
from plugins import bind_plugins, current_user, logger, db, init
from routers import bind_routers

# ==================================================
# ! SERVER INIT
# ==================================================

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('SEC_KEY')

# ==================================================
# & EXTENSIONS BINDING
# ==================================================

bind_plugins(server)
bind_routers(server)

# ==================================================
# ! DB INIT
# ==================================================

with server.app_context():
    if (not os.path.exists('migrations')): init()
    db.create_all()

# ==================================================
# & INITIAL ROUTES
# ==================================================

# & USER LOADER
@logger.user_loader
def load_user(user):
    return User.query.get(user)

@server.route('/')
def initialize():
    if (current_user.is_authenticated):
        return redirect(url_for('app.index'))
    return redirect(url_for('auth.index'))
