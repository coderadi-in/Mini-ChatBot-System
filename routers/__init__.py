# ==================================================
# ? IMPORTS
# ==================================================

from .app import app

# ==================================================
# * FUNCTIONS
# ==================================================

# * FUNCTION TO BIND ROUTES TO THE SERVER
def bind_routers(server):
    '''Binds all routers to the server.'''

    server.register_blueprint(app)

# ==================================================
# ! FILE OUTPUT LIST
# ==================================================

__all__ = [ 'bind_routers', 'app' ]