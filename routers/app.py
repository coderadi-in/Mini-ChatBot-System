# ==================================================
# ? IMPORTS
# ==================================================

from flask import Blueprint, render_template, redirect, url_for
from plugins import *

# ==================================================
# ! ROUTER INIT
# ==================================================

app = Blueprint('app', __name__, url_prefix='/app')

# ==================================================
# & END POINTS
# ==================================================

# & BASE ROUTE
@app.route('/')
def index():
    # RETURN RESPONSE
    return render_template('pages/index.html')