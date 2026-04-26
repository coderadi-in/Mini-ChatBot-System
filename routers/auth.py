# ==================================================
# ? IMPORTS
# ==================================================

from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import encoder, db, login_user, logout_user, current_user
from models import *

# ==================================================
# ! ROUTER INIT
# ==================================================

auth = Blueprint('auth', __name__, url_prefix='/auth')

# ==================================================
# & END POINTS
# ==================================================

# & BASE ROUTE
@auth.route('/',)
def index():
    return render_template('auth/log.html')

# & SIGNUP ROUTE
@auth.route('/signup', methods=['POST'])
def signup():
    # ACCESS FORM ELEMENTS
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # DATA VALIDATION
    if (not name or not email or not password):
        flash("One or more required inputs aren't provided!", "error")
        return redirect(url_for('auth.index'))
    
    if (User.query.filter_by(email=email).first() is not None):
        flash("This email is already linked to a chatbot account!", "error")
        return redirect(url_for('auth.index'))
    
    # PASSWORD HASHING
    hashed_password = encoder.generate_password_hash(password)

    # CREATE NEW USER MODEL
    new_user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    # ADD NEW USER TO DB
    db.session.add(new_user)
    db.session.commit()

    # REDIRECT USER TO CHAT PAGE
    flash("Welcome to chatbot!", "waving_hand")
    return redirect(url_for('app.index'))

# & LOGIN ROUTE
@auth.route('/login', methods=['POST'])
def login():
    # ACCESS FORM ELEMENTS
    email = request.form.get('email')
    password = request.form.get('password')

    # DATA VALIDATION
    if (not email or not password):
        flash("One or more required inputs aren't provided!", "error")
        return redirect(url_for('auth.index'))
    
    logged_user = User.query.filter_by(email=email).first()

    if (not logged_user):
        flash("This email is not linked to any chatbot account!", "error")
        return redirect(url_for('auth.index'))
    
    if (not encoder.check_password_hash(logged_user.password, password)):
        flash("Password mismatched!", "error")
        return redirect(url_for('auth.index'))

    # LOGIN USER
    login_user(logged_user)

    # REDIRECT USER TO CHAT PAGE
    flash("Welcome back to chatbot!", "waving_hand")
    return redirect(url_for('app.index'))