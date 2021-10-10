"""
here we'll
activate our app instance
"""

from app import app, routes

if __name__ == '__main__':
    app.register_blueprint(routes)
    app.run()
