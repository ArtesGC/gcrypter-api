"""
here we'll
define our virtual-variables
as configuration to our project
"""


class Config:
    """project's configuration"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/gc.db'
