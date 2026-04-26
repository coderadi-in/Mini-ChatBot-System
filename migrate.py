# ==================================================
# ? IMPORTS
# ==================================================

from main import server
from plugins import migrate, upgrade

# ==================================================
# ! MIGRATIONS
# ==================================================

with server.app_context():
    migrate('migrations')
    upgrade('migrations')