from flask import Blueprint, render_template, request

# Create a blueprint for the main application
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return '<h1>Welcome to the Movie Search Platform</h1>'