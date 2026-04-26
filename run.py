# ==================================================
# ? IMPORTS
# ==================================================

from plugins import socket
from main import server

# ==================================================
# ! RUN COMMAND
# ==================================================

if (__name__ == "__main__"):
    socket.run(server, debug=True, host='0.0.0.0', allow_unsafe_werkzeug=True)