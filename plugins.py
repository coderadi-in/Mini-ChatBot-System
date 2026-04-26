# ==================================================
# ? IMPORTS
# ==================================================

from flask_socketio import SocketIO, emit

# ==================================================
# ! PLUGINS INIT
# ==================================================

socket = SocketIO()

# ==================================================
# * FUNCTIONS
# ==================================================

# * FUNCTION TO BIND ALL PLUGINS TO THE SERVER
def bind_plugins(server):
    '''Binds all plugins to the server.'''

    socket.init_app(server)

# ==================================================
# ! FILE OUTPUT LIST
# ==================================================

__all__ = [ 'bind_plugins', 'socket' ]