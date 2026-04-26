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
from plugins import bind_plugins
from routers import bind_routers

# ==================================================
# ! SERVER INIT
# ==================================================

server = Flask(__name__)
server.config['SECRET_KEY'] = os.getenv('SEC_KEY')

# ==================================================
# & EXTENSIONS BINDING
# ==================================================

bind_plugins(server)
bind_routers(server)

# ==================================================
# & INITIAL ROUTE
# ==================================================

@server.route('/')
def initialize():
    return redirect(url_for('app.index'))
