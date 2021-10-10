"""
here goes all
definition of our app instance
"""

from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routers
