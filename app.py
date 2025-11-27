# app.py

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def hello_world():
    """Returns a simple greeting message for the home page."""
    return '<h1>Hello, World!</h1><p>This is a simple Python web app.</p>'

# You can add more routes and functions here

# For example, an 'about' page
@app.route('/about')
def about():
    """Returns content for the about page."""
    return '<h1>About Us</h1><p>We are learning to build web apps with Python Flask!</p>'

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0',debug=True)
