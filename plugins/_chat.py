# ==================================================
# ? IMPORTS
# ==================================================

from . import socket, get_response

# ==================================================
# & EVENTS
# ==================================================

# & SEND EVENT
@socket.on('send')
def recv_message(message):
    response = get_response(message)
    socket.emit('recv', response)
