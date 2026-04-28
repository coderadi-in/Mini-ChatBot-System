# ==================================================
# ? IMPORTS
# ==================================================

from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *
from models import *

# ==================================================
# ! ROUTER INIT
# ==================================================

account = Blueprint('account', __name__, url_prefix='/account')

# ==================================================
# & END POINTS
# ==================================================

# & UPDATE PROFILE ENDPOINT
@account.route('/update/profile', methods=['POST'])
def update_profile():
    # ACCESS FORM DATA
    name = request.form.get('name', current_user.name)
    email = request.form.get('email', current_user.email)

    # EMAIL VALIDATION
    if (User.query.filter_by(email=email).first() is not None):
        flash("This email is already linked to a chatbot account!", "error")
        redirect(redirect(url_for('app.index')))

    # UPDATE PROFILE
    current_user.name = name
    current_user.email = email

    # UPDATE DATABASE
    db.session.commit()

    # RETURN RESPONSE
    flash("Your account has been updated.", "check_circle")
    return redirect(url_for('app.index'))

# & UPDATE INSTRUCTIONS ENDPOINT
@account.route('/update/instructions', methods=['POST'])
def update_instructions():
    # ACCESS FORM DATA
    role = request.form.get('role', current_user.ai_role)
    language = request.form.get('language', current_user.ai_language)
    nickname = request.form.get('nickname', current_user.nickname)
    work = request.form.get('work', current_user.work)

    # BUILD CUSTOM INSTRUCTION PROMPT
    custom_instruction = f'''You have to talk to the user as a/an {role} in {language} language.
User wants you to call him/her {nickname} and has mentioned following occupation:
{work}'''
    
    # UPDATE INSTRUCTION
    current_user.ai_role = role
    current_user.ai_language = language
    current_user.nickname = nickname
    current_user.work = work
    current_user.custom_instructions = custom_instruction
    db.session.commit()

    # RETURN RESPONSE
    flash("You're AI settings has been updated.", "check_circle")
    return redirect(url_for('app.index'))