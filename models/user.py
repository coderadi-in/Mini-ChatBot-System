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
    ai_role = db.Column(db.String, default="Friend")
    ai_language = db.Column(db.String, default="English")
    nickname = db.Column(db.String)
    work = db.Column(db.String)
    custom_instructions = db.Column(
        db.TEXT,
        default="""You have to talk to the user as a/an Friend.
Use English language tone to talk.""",
    )
