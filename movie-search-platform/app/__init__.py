from flask import Flask

def create_app():
    # This function creates an instance of the Flask application
    app = Flask(__name__)

    from .routes import main

    # Register the main blueprint with the application
    app.register_blueprint(main) 

    return app