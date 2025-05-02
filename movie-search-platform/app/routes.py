from flask import Blueprint, render_template, request

# Create a blueprint for the main application
main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Render the home page
    return render_template('home.html')