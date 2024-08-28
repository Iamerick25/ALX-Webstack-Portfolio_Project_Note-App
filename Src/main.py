#!/home/elysee_niyibizi/note-app/venv/bin/python

"""
Script to run the Flask web application.
"""

from website import create_app  # Import the create_app function from the website package

app = create_app()  # Create the Flask application using the create_app function

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
