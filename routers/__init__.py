# ==================================================
# ? IMPORTS
# ==================================================

from .app import app
from .auth import auth
from .account import account

# ==================================================
# * FUNCTIONS
# ==================================================

# * FUNCTION TO BIND ROUTES TO THE SERVER
def bind_routers(server):
    '''Binds all routers to the server.'''

    server.register_blueprint(app)
    server.register_blueprint(auth)
    server.register_blueprint(account)