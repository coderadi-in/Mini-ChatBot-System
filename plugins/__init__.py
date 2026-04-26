# ==================================================
# ? IMPORTS
# ==================================================

from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_migrate import Migrate, migrate, init, upgrade
from flask_bcrypt import Bcrypt
from openai import OpenAI
import os

# ==================================================
# ! PLUGINS INIT
# ==================================================

socket = SocketIO()
db = SQLAlchemy()
logger = LoginManager()
migrator = Migrate()
encoder = Bcrypt()

# ==================================================
# * FUNCTIONS
# ==================================================


# * FUNCTION TO BIND ALL PLUGINS TO THE SERVER
def bind_plugins(server):
    """Binds all plugins to the server."""

    socket.init_app(server)
    db.init_app(server)
    logger.init_app(server)
    migrator.init_app(server, db)
    encoder.init_app(server)


# * FUNCTION TO SEND MESSAGE TO MODEL
def get_response(message):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        socket.emit("recv", "There're issues in the backend!")
        raise RuntimeError(
            "OPENAI_API_KEY is missing. Add it to .venv/vars.env or your environment variables."
        )

    try:
        model = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        response = model.responses.create(
            model="gpt-5.1",
            input=[
                {
                    "role": "system",
                    "content": "You've to give small responses, and talk like an old friend in HINGLISH.",
                },
                {"role": "user", "content": message},
            ],
            temperature=0.7,
            max_output_tokens=500,
        )

        return response.output_text

    except Exception as e:
        socket.emit("recv", "Something went wrong while generating response!")


# ==================================================
# ! INTEGRATE CHAT EVENT HANDLERS
# ==================================================

from . import _chat