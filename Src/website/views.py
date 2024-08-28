from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """Renders the home page where users can view and add notes."""
    if request.method == 'POST':  # If the request method is POST
        note = request.form.get('note')  # Get the note data from the HTML form

        if len(note) < 1:  # Check if the note is too short
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)  # Create a new Note object with the provided data and user id
            db.session.add(new_note)  # Add the new note to the database
            db.session.commit()  # Commit the changes to the database
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    """Deletes a note."""
    note = json.loads(request.data)  # Parse the JSON data from the request
    noteId = note['noteId']  # Get the ID of the note to be deleted
    note = Note.query.get(noteId)  # Retrieve the note from the database

    if note:
        if note.user_id == current_user.id:  # Check if the current user owns the note
            db.session.delete(note)  # Delete the note from the database
            db.session.commit()  # Commit the changes to the database

    return jsonify({})  # Return an empty JSON response
