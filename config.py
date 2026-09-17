import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "washington-oliveira-dev-key")
    DATABASE = os.path.join(os.path.dirname(__file__), "instance", "portfolio.sqlite3")
