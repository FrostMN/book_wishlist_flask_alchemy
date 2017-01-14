DEBUG = True     # Turns logging features on for code. Separate to the in-browser debugger and code-relaucher.
SQLALCHEMY_DATABASE_URI = 'sqlite:///wishlist.db'   # /// relative path to this app.    # //// absolute path to somewhere on file system
SECRET_KEY = 'super random secret value'
SEND_FILE_MAX_AGE_DEFAULT = 30 # How long to cache static files for. Working??
