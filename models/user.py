# ==================================================
# ? IMPORTS
# ==================================================

from plugins import *

# ==================================================
# & DB MODEL DEFINITION
# ==================================================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    custom_instructions = db.Column(db.TEXT)